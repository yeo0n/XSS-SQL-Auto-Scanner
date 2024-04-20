
# 필요한 라이브러리를 임포트합니다.
import requests
from urllib.parse import urljoin, urlparse, parse_qs
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_COMPLETED
from multiprocessing import Manager
from xss_test import test_xss  # xss_test 모듈에서 test_xss 함수를 임포트합니다.

# 각 페이지를 크롤링하는 함수입니다.
def crawl_page(url, visited, collected_urls_params, payloads):
    try:
        # 페이지에 요청을 보냅니다.
        headers = {"User-Agent": "Mozilla/5.0"}
        for _ in range(3):  # 재시도 로직을 추가합니다.
            try:
                response = requests.get(url, headers=headers)
                break
            except:
                print(f"Retry: {url}")
        else:
            print(f"Failed to fetch: {url}")
            return url, []

        # BeautifulSoup 객체를 생성하여 HTML을 파싱합니다.
        soup = BeautifulSoup(response.text, 'html.parser')

        for a_url in soup.find_all('a'):
            name = a_url.get('href')
            if name:
                param_url=f'{urlparse(url)._replace(query="").geturl()}'
                if param_url not in collected_urls_params:
                    collected_urls_params.append(param_url)
                    print(param_url)
                    test_xss(param_url, payloads)

        # 페이지 내에서 발견한 모든 링크를 수집합니다.
        links = [urljoin(url, link.get('href')) for link in soup.find_all('a') if urljoin(url, link.get('href')) not in visited]

        # 현재 페이지 URL과 수집한 링크를 반환합니다.
        return url, links
    except Exception as e:
        # 오류가 발생한 경우, 오류 메시지를 출력하고 현재 페이지 URL과 빈 링크 리스트를 반환합니다.
        print(f"Error occurred: {e}")
        return url, []

# 웹사이트를 크롤링하는 함수입니다.
def crawl_website(start_url, paylaods):
    with Manager() as manager:
        # 방문한 페이지와 수집한 URL과 파라미터의 쌍을 저장하는 리스트를 생성합니다.
        visited = manager.list([start_url])
        collected_urls_params = manager.list()

        # 시작 URL의 도메인을 파싱합니다.
        parsed_start_url = urlparse(start_url)
        start_domain = parsed_start_url.netloc

        # ProcessPoolExecutor를 사용하여 병렬로 페이지를 크롤링합니다.
        with ProcessPoolExecutor(max_workers=8) as executor:
            futures = {executor.submit(crawl_page, start_url, visited, collected_urls_params, paylaods)}
            while futures:
                # 완료된 작업을 기다립니다.
                done, futures = wait(futures, return_when=FIRST_COMPLETED)
                for future in done:
                    _, links = future.result()
                    for link in links:
                        # 링크가 아직 방문하지 않은 링크이고 같은 도메인에 속하는 경우, 그 링크를 크롤링합니다.
                        if link not in visited and urlparse(link).netloc == start_domain:
                            visited.append(link)
                            futures.add(executor.submit(crawl_page, link, visited, collected_urls_params, paylaods))