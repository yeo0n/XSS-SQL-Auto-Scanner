import sys
import time

print("\n해당 섹션은 보기에 대한 설명을 시작합니다.")
time.sleep(1)
a=1
while (a<4):
    print(".\n")
    time.sleep(0.5)
    a+=1

while(True):
    print("1. 취약점 진단 시작")
    print("ㄴ> SQL Injection, XSS 의 취약점들을 진단합니다.")
    print("2. 도구 프로그램 사용법")
    print("ㄴ> 취약점을 진단할 도메인을 입력한 후, 자동으로 취약점 진단을 시작합니다.")
    print("3. 팀 소개 및 개발배경")
    print("ㄴ> TEAM . 웹 취약점에 관심이 많아 개발하게된 팀에 대해서 설명합니다.")
    print("4. 보기 설명")
    print("ㄴ> 이는 보기에 대한 설명입니다. 본 섹션이 이에 해당합니다.")
    print("5. 맞춤형 대화 인터페이스")
    print("ㄴ> 대화를 시작하여 예, 아니오를 통해 맞춰나가는 인터페이스입니다.")
    print("0. 프로그램 종료")
    print("ㄴ>프로그램이 종료됩니다.")
    
    print("\n")
    
    b=input("메인메뉴로 돌아가고 싶다면 q를 입력해주세요 :")
    if (b=="q"):
        break
    else :
        print("\n========q를 입력해주세요.========\n")
