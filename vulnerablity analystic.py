import sys
import os
import time
import subprocess
from createPDF import *
from XSS.xss_test import load_data_from_file
from XSS.xss_test import load_rxss
from StoredXSS.xss_test import load_sxss
from DOM_XSS.xss_test import load_dxss
from Normal_SQLi.normal_sqli2 import load_nsql
from Blind_SQLi.blind_sqli import load_bsql

def num1():
    # Reflected XSS [ 반사된 XSS 진단 시작 ]
    print("\n Reflected XSS 취약점 진단을 시작합니다. \n")
    subprocess.run(["python", "XSS/main.py"])

def num2():
    # Stored XSS [ 저장된 XSS 진단 시작 ]
    print("\n Stored XSS 취약점 진단을 시작합니다. \n")
    subprocess.run(["python", "StoredXSS/main.py"])

def num3():
    # DOM XSS [ DOM 베이스 XSS 진단 시작 ]
    print("\n DOM Based XSS 취약점 진단을 시작합니다. \n")
    subprocess.run(["python", "DOM_XSS/main.py"])

def num4():
    # Normal SQLi [ SQL 인젝션 진단 시작 ]
    print("\n Normal SQLi 취약점 진단을 시작합니다. \n")
    subprocess.run(["python", "Normal_SQLi/normal_sqli2.py"])

def num5():
    # Blind SQLi [ 블라인드 SQL 인젝션 진단 시작 ]
    print("\n Blind SQLi 취약점 진단을 시작합니다. \n")
    subprocess.run(["python", "Blind_SQLi/blind_sqli.py"])

print("\n")
print("=========================================================================================================")
print("-> \033[33m크로스 사이트 스크립팅 (XSS)\033[0m 이란? <-")
print("사용자가 웹사이트와 상호작용할 때 비정상적인 상황을 발생시킵니다.")
print("이는 또한 \033[38;2;255;0;0m공격자\033[0m가 피해자 사용자로 가장하여 사용자의 권한을 갖고 권한 내의 피해를 발생시킬 수 있습니다.")
print("쉽게 말해서 \033[38;2;255;0;0m공격자\033[0m가 사용자의 권한을 갖고 모든 기능과 데이터에 대한 제어권을 얻어낼 수 있습니다.")

print("\n")
print("-> \033[33mSQL 인젝션 (SQLi)\033[0m 이란? <-")
print("웹사이트가 데이터베이스에 상호작용 할 때 방해할 수 있는 보안 취약점입니다.")
print("쉽게 말해서 \033[38;2;255;0;0m공격자\033[0m가 데이터를 가지고 수정하거나 삭제하거나 기밀 문서를 유출할 수 있습니다.")
print("=========================================================================================================")

while(True):
    
    print("\n 원하는 취약점 진단 분야를 선택해주세요.")
    print("(보기의 ALL은 해당 취약점의 종류를 모두 검사합니다.)")
    time.sleep(1)

    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃     1. Reflected XSS       ┃")
    print("┃     2. Stored XSS          ┃")
    print("┃     3. DOM XSS             ┃")
    print("┃     4. Normal SQLi         ┃")
    print("┃     5. Blind SQLi          ┃")
    print("┠━━━━━━━━━━━━━━━━━━━━━━━━━━━━┨")
    print("┃     6. ALL XSS             ┃")
    print("┃     7. ALL SQLi            ┃")
    print("┃     8. ALL SCAN            ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("\n")
    print(" \033[33m메인메뉴로 돌아가고 싶다면 0 을 입력해주세요 \033[0m")
        
        
        
    try :
        choiceMenu = int(input("\n번호 선택 : "))
        if choiceMenu == 1:
            # 1번 선택
            num1()
            print("")
            xy = input("보고서를 생성하시겠습니까? (Y/y, N/n): ")
            if xy == "Y" or "y":
                inputURL = load_data_from_file('url.json') # url.json 파일에서 도메인 읽어오기
                collectVul = ["Reflected XSS"]
                RXSS = load_data_from_file('rxss_data.json')
                create_pdf("XSAS Results Report.pdf", inputURL, collectVul, RXSS)
                print(f"보고서가 {os.path.dirname(os.path.realpath(__file__))} 경로에 생성되었습니다.")
        elif choiceMenu == 2:
            # 2번 선택
            num2()
            print("")
            xy = input("보고서를 생성하시겠습니까? (Y/y, N/n): ")
            if xy == "Y" or "y":
                inputURL = load_data_from_file('url.json') # url.json 파일에서 도메인 읽어오기
                collectVul = ["Stored XSS"]
                RXSS = []
                SXSS = load_sxss()
                create_pdf("XSAS Results Report.pdf", inputURL, collectVul, RXSS, SXSS)
                print(f"보고서가 {os.path.dirname(os.path.realpath(__file__))} 경로에 생성되었습니다.")
        elif choiceMenu == 3:
            # 3번 선택
            num3()
            print("")
            xy = input("보고서를 생성하시겠습니까? (Y/y, N/n): ")
            if xy == "Y" or "y":
                inputURL = load_data_from_file('url.json') # url.json 파일에서 도메인 읽어오기
                collectVul = ["DOM XSS"]
                RXSS = []
                SXSS = []
                DXSS = load_dxss()
                create_pdf("XSAS Results Report.pdf", inputURL, collectVul, RXSS, SXSS, DXSS)
                print(f"보고서가 {os.path.dirname(os.path.realpath(__file__))} 경로에 생성되었습니다.")
        elif choiceMenu == 4:
            # 4번 선택
            num4()
            print("")
            xy = input("보고서를 생성하시겠습니까? (Y/y, N/n): ")
            if xy == "Y" or "y":
                inputURL = input("점검하신 도메인을 입력하세요: ")
                collectVul = ["Normal SQLi"]
                RXSS = []
                SXSS = []
                DXSS = []
                NSQL = load_nsql()
                create_pdf("XSAS Results Report.pdf", inputURL, collectVul, RXSS, SXSS, DXSS, NSQL)
                print(f"보고서가 {os.path.dirname(os.path.realpath(__file__))} 경로에 생성되었습니다.")
        elif choiceMenu == 5:
            # 5번 선택
            num5()
            print("")
            xy = input("보고서를 생성하시겠습니까? (Y/y, N/n): ")
            if xy == "Y" or "y":
                inputURL = input("점검하신 도메인을 입력하세요: ")
                collectVul = ["Blind SQLi"]
                RXSS = []
                SXSS = []
                DXSS = []
                NSQL = []
                BSQL = load_bsql()
                create_pdf("XSAS Results Report.pdf", inputURL, collectVul, RXSS, SXSS, DXSS, NSQL, BSQL)
                print(f"보고서가 {os.path.dirname(os.path.realpath(__file__))} 경로에 생성되었습니다.")
        elif choiceMenu == 6:
            # 6번 선택
            num1()
            num3()
            num2()
            print("")
            xy = input("보고서를 생성하시겠습니까? (Y/y, N/n): ")
            if xy == "Y" or "y":
                inputURL = load_data_from_file('url.json') # url.json 파일에서 도메인 읽어오기
                collectVul = ["Reflected XSS", "Stored XSS", "DOM XSS"]
                RXSS = load_data_from_file('rxss_data.json')
                SXSS = load_sxss()
                DXSS = load_dxss()
                create_pdf("XSAS Results Report.pdf", inputURL, collectVul, RXSS, SXSS, DXSS)
                print(f"보고서가 {os.path.dirname(os.path.realpath(__file__))} 경로에 생성되었습니다.")
        elif choiceMenu == 7:
            # 7번 선택
            num4()
            num5()
            print("")
            xy = input("보고서를 생성하시겠습니까?: (Y/y, N/n): ")
            if xy == "Y" or "y":
                inputURL = input("점검하신 도메인을 입력하세요: ")
                collectVul = ["Normal SQLi", "Blind SQLi"]
                RXSS = []
                SXSS = []
                DXSS = []
                NSQL = load_nsql()
                BSQL = load_bsql()
                create_pdf("XSAS Results Report.pdf", inputURL, collectVul, RXSS, SXSS, DXSS, NSQL, BSQL)
                print(f"보고서가 {os.path.dirname(os.path.realpath(__file__))} 경로에 생성되었습니다.")
        elif choiceMenu == 8:
            # 8번 선택
            num1()
            num3()
            num2()
            num4()
            num5()
            print("")
            xy = input("보고서를 생성하시겠습니까?: (Y/y, N/n): ")
            if xy == "Y" or "y":
                inputURL = load_data_from_file('url.json') # url.json 파일에서 도메인 읽어오기
                collectVul = ["Reflected XSS", "Stored XSS", "DOM XSS", "Normal SQLi", "Blind SQLi"]
                RXSS = load_data_from_file('rxss_data.json')
                SXSS = load_sxss()
                DXSS = load_dxss()
                NSQL = load_nsql()
                BSQL = load_bsql()
                create_pdf("XSAS Results Report.pdf", inputURL, collectVul, RXSS, SXSS, DXSS, NSQL, BSQL)
                print(f"보고서가 {os.path.dirname(os.path.realpath(__file__))} 경로에 생성되었습니다.")
        elif choiceMenu == 0:
            #0 프로그램 종료
            print("\n프로그램을 종료합니다.\n")
            break
        else:
            print("\n잘못된 번호를 입력했습니다.\n")
            time.sleep(1)
    except ValueError :
        print("\n숫자를 입력해주세요.\n")
        time.sleep(1)
