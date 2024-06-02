# 필요한 모듈들을 임포트합니다.
import json
from urllib.parse import quote
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

RXSS = []
RXSS_FILE = 'rxss_data.json'

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # 파일이 없을 경우 빈 리스트를 반환

def save_rxss():
    global RXSS
    save_data_to_file(RXSS, RXSS_FILE)

def load_rxss():
    global RXSS
    RXSS = load_data_from_file(RXSS_FILE)

# XSS 페이로드를 로드하는 함수입니다.
def load_xss_paylaods(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def test_single_payload(url, payload):
    global RXSS
    try:
        # 페이로드를 URL에 추가하여 GET 요청을 보냅니다.
        # 페이로드를 URL 인코딩합니다.
        response = requests.get(url + quote(payload))

        # 페이로드가 응답에 포함되어 있는지 확인합니다.
        if payload in response.text:
            print(f"[R] {url}{quote(payload)}")

        # Selenium을 사용하여 웹 페이지를 로드하고, 페이지에 alert 창이 띄워져 있는지 확인합니다.
        # 웹드라이버 인스턴스를 각 작업마다 새로 생성합니다.
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(url + quote(payload))
        alert_present = False
        try:
            # WebDriverWait를 사용하여 페이지가 완전히 로드될 때까지 기다립니다.
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert_present = True
        except:
            pass
        
        # alert 창이 띄워져 있다면, XSS 취약점이 발견되었다고 보고합니다.
        if alert_present:
            print(f"🛑 \033[38;2;255;0;0m[V] {url}{quote(payload)}\033[0m")
            RXSS.append(url + quote(payload))
            save_data_to_file(RXSS, RXSS_FILE)

        # 웹드라이버 인스턴스를 종료합니다.
        driver.quit()
    except Exception as e:
        print(f"🟡 An error occurred while testing the payload: {e}")

def test_xss(url, payloads):
    for payload in payloads:
        test_single_payload(url, payload)
