# 필요한 모듈들을 임포트합니다.
from urllib.parse import quote
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Pool
from selenium.webdriver.common.by import By
import json

SXSS = []
SXSS_FILE = 'sxss_data.json'

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # 파일이 없을 경우 빈 리스트를 반환

def save_sxss():
    global SXSS
    save_data_to_file(SXSS, SXSS_FILE)

def load_sxss():
    return load_data_from_file(SXSS_FILE)

# XSS 페이로드를 로드하는 함수입니다.
def load_xss_paylaods(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
    
def test_single_payload(args):
    global SXSS
    url, payload = args
    try:
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(url)
        alert_present = False
        try:
            text_element = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
            text_element.send_keys(payload)

            textarea_element = driver.find_element(By.CSS_SELECTOR, "textarea")
            textarea_element.send_keys(payload)

            submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            submit.click()
            # WebDriverWait를 사용하여 페이지가 완전히 로드될 때까지 기다립니다.
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert_present = True
        except:
            pass
        # alert 창이 띄워져 있다면, XSS 취약점이 발견되었다고 보고합니다.
        if alert_present:
            print(f"🛑 \033[38;2;255;0;0m[V] {url}{quote(payload)}\033[0m")
            SXSS.append(url + quote(payload))
            save_data_to_file(SXSS, SXSS_FILE)
            save_sxss()

        # 웹드라이버 인스턴스를 종료합니다.
        driver.quit()
    except Exception as e:
        print(f"An error occurred while testing the payload: {e}")

def test_xss(url, payloads):
    for payload in payloads:
        test_single_payload((url, payload))