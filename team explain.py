import sys
import time

print("\n해당 섹션은 팀 소개 및 개발배경에 대한 설명을 시작합니다.")
time.sleep(1)

while(True):
    print("\n==========================\033[94m| Team.XSAS |\033[0m==========================\n")
    print("                          1921009  김우현                       \n")
    print("                          1921015  박연준                       \n")    
    print("                          1921035  전태현                       \n")
    print("                     -경동대학교 정보보안학과-                   \n")
    print("\n==========================\033[94m| 개발 동기 |\033[0m==========================\n")
    print(" 해킹 사고 중 웹 해킹의 비중이 높게 차지하고 있습니다.\n") 
    print(" 저희는 웹 취약점 분석 도구 개발을 통해 웹 해킹에 대해 \n")
    print(" 깊게 알아가고자 개발을 진행했습니다.                 \n")
    print("\n XSAS는 대화형 인터페이스를 통해 사용자에게 알기쉽고 편하게 취약점을 \n")
    print(" 진단하고 보고서를 생성하여 이메일로 제공해주는 것을 목표로 두고 \n")
    print(" 개발을 진행하였습니다. \n")   
    print("\n==================================================================\n")
    b=input("메인메뉴로 돌아가고 싶다면 q를 입력해주세요 :")
    if (b=="q"):
        break
    else :
        print("\n========q를 입력해주세요.========\n")