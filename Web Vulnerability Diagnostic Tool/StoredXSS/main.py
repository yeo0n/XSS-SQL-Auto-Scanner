# 메인 실행 코드

from xss_test import load_xss_paylaods  # xss_test 모듈에서 load_xss_payloads 함수를 임포트합니다.
from web_crawler import crawl_website  # web_crawler 모듈에서 crawl_website 함수를 임포트합니다.
from xss_test import *

startUrl = []
startUrl_FILE = 'url.json'

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # 파일이 없을 경우 빈 리스트를 반환

def save_starturl():
    global startUrl
    save_data_to_file(startUrl, startUrl_FILE)

def load_startUrl():
    return load_data_from_file(startUrl_FILE)

def main():
    # 사용자로부터 시작 URL을 입력받습니다.
    start_url = input("Enter a domain: ")
    startUrl.append(start_url)
    save_starturl()
    print()
    # XSS 페이로드를 로드합니다.
    payloads = load_xss_paylaods("StoredXSS/payload.txt")
    # 입력받은 URL을 기준으로 웹사이트를 크롤링합니다.
    crawl_website(start_url, payloads)
    
if __name__ == '__main__':
    main()
