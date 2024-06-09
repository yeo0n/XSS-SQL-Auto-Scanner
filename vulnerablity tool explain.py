import sys
import time

print("\n해당 섹션은 도구 프로그램 사용법에 대한 설명을 시작합니다.")
time.sleep(1)

while(True):
    print("\n=========================\033[94m| 도구 사용법 |\033[0m=========================\n")
    print(" \033[94m선택 1\033[0m : 취약점 진단 시작\n")
    print("       -> 진단할 URL 입력해주세요. (예시 : https://naver.com) \n")
    print("       -> 보고서 전달받을 Email 입력해주세요. (예시 : user1234@naver.com) \n")
    print("       -> 진단이 완료되면 해당 이메일로 진단 보고서가 PDF 형식으로 전송됩니다.\n")    
    print("\n==========================\033[94m| 점검 항목 |\033[0m==========================\n")
    print("1. SQL injection \n")
    print("   웹페이지 내 SQL injection 취약점 존재 여부를 점검합니다.\n")
    print("2. XSS (크로스사이트 스크립팅) \n")
    print("   웹 사이트 내 크로스사이트 스크립팅 취약점 존재 여부를 점검합니다.\n")
    print("\n==================================================================\n")
    
    b=input("메인메뉴로 돌아가고 싶다면 q를 입력해주세요 :")
    if (b=="q"):
        break
    else :
        print("\n========q를 입력해주세요.========\n")