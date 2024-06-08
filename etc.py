import sys
import time

print("\n해당 섹션은 맞춤형 대화 인터페이스입니다.")
time.sleep(1)

print("\n")

print("🔘 아래부터는 대화를 진행하여 해당 취약점을 검사해야하는지에 대해 간단히 알아보겠습니다.")
print("🔘 대화는 예 (Y/y) / 아니오 (N/n) 로만 진행되며, 선택지가 얼마나 있는지에 대해서 표기해드립니다.")
print("🔘 테스트 할 웹사이트 (이하 TW) 를 하나 정하신 다음에 대화를 진행해주세요.")

print("\n")
time.sleep(1)

def num1():
    print("\n선택하신 TW 를 기준으로 \033[33mXSS\033[0m 취약점 검사 적합성에 대해 문답을 진행합니다.")
    print("✅ 진행할 문답은 총 5 개 입니다.")
    time.sleep(2)
    
    countxss = 0
    
    select = input("\n1️⃣  커뮤니티와 같은 게시판 기능을 사용하는 TW 인가요? Y/N : ")
    if select == 'y' or select == 'Y':
        countxss += 1
    
    select = input("\n2️⃣  관리자 권한을 얻었을 때, 초래할수 있는 잠재적 위협이 큰 편인가요? Y/N : ")
    if select == 'y' or select == 'Y':
        countxss += 1
    
    select = input("\n3️⃣  TW 가 악성적인 링크 또는 광고에 취약한 편인가요? Y/N : ")
    if select == 'y' or select == 'Y':
        countxss += 1
    
    select = input("\n4️⃣  세션, 쿠키를 자주 사용하는 TW 인가요? Y/N : ")
    if select == 'y' or select == 'Y':
        countxss += 1
        
    select = input("\n5️⃣  아이디와 비밀번호를 입력하여 로그인하는 TW 인가요? Y/N : ")
    if select == 'y' or select == 'Y':
        countxss += 1
    
    print("\n=========================================================")
    
    time.sleep(2)
    print("진행한 문답에 따라 나온 결과 점수는 ",countxss,"점 입니다.")
    if countxss >= 3:
        print("🔴 선택한 \033[38;2;255;0;0mTW\033[0m 는 \033[33mXSS\033[0m 취약점 진단을 필요로 합니다.")
    else :
        print("🟢 선택한 \033[92mTW\033[0m 는 \033[33mXSS\033[0m 취약점 진단이 급한 수준이 아닙니다.")
        
        
    print("=========================================================")
    print("\n")
    time.sleep(3)
    

def num2():
    print("\n선택하신 TW 를 기준으로 \033[33mSQLi\033[0m 취약점 검사 적합성에 대해 문답을 진행합니다.")
    print("✅ 진행할 문답은 총 5 개 입니다.")
    time.sleep(2)
    
    countsql = 0
    
    select = input("\n1️⃣  온라인 은행이나 결제 시스템과 같은 2차 비밀번호 & 신용카드 정보 등을 다루는 TW 인가요? Y/N : ")
    if select == 'y' or select == 'Y':
        countsql += 1
    
    select = input("\n2️⃣  데이터베이스에 민감한 정보가 포함되어 있는 TW 인가요? Y/N : ")
    if select == 'y' or select == 'Y':
        countsql += 1
    
    select = input("\n3️⃣  데이터베이스나 서버 과부하가 발생했을 시 서비스가 중단되면 손해가 큰 편인가요? Y/N : ")
    if select == 'y' or select == 'Y':
        countsql += 1
    
    select = input("\n4️⃣  데이터베이스의 내용이 변경되었을 시 초래할 수 있는 잠재적 위협이 큰 편인가요? Y/N : ")
    if select == 'y' or select == 'Y':
        countsql += 1
    
    select = input("\n5️⃣  아이디와 비밀번호를 입력하여 로그인하는 TW 인가요? Y/N : ")
    if select == 'y' or select == 'Y':
        countsql += 1
    
    print("\n=========================================================")
    
    time.sleep(2)        
    print("진행한 문답에 따라 나온 결과 점수는 ",countsql,"점 입니다.")
    if countsql >= 3:
        print("🔴 선택한 \033[38;2;255;0;0mTW\033[0m 는 \033[33mSQLi\033[0m 취약점 진단을 필요로 합니다.")
    else :
        print("🟢 선택한 \033[92mTW\033[0m 는 \033[33mSQLi\033[0m 취약점 진단이 급한 수준이 아닙니다.")
    
    
    print("=========================================================")
    print("\n")
    time.sleep(3)
    
    
    
# XSS, SQLi 로 구분지었지만, Reflected / Stored / DOM / Normal / Blind 으로 구분지어야함.

# Reflected 공격 핵심 -> 사용자에게 입력 받은 값을 서버에서 되돌려주는 곳에서 발생
# ㄴ> 피해자에게 입력한 값을 오류 메시지와 함께 보여주는 곳에 악성 스크립트 삽입
# Stored 공격 핵심 -> 삽입된 스크립트가 데이터베이스에 저장
# ㄴ> 해당 게시글 등을 열람하면 쿠키 탈취, 타사이트 리디렉션 공격을 받음
# DOM 공격 핵심 -> 피해자의 브라우저에 초점을 맞춘 공격
# ㄴ> 서버와 상호작용이 아닌 웹페이지를 여는 즉시 생성되는 문서객체모델 (DOM) 을 통해 공격 (웹사이트코드조사 필요)

# Normal 공격 핵심 -> SQL 쿼리문이 여러 입력폼에 입력되어 데이터가 전송됨
# ㄴ> SQL 쿼리문을 통해 전송되어 데이터를 조작함
# Blind 공격 핵심 -> DB 메시지가 보이진 않지만, 참과 거짓의 반응만을 이용해 데이터를 얻어냄
# ㄴ> 계속해서 질의를 보내 참과 거짓을 비교하여 소거법을 적용하여 특정 데이터를 추출하는 방법

while(True):
    
    print("\n원하는 취약점 유형에 대해서 대화하시려면 문자를 입력해주세요.\n")
    print("<================================================>")
    print("    1. XSS (크로스 사이트 스크립팅) 에 대해서")
    print("    2. SQLi (SQL 인젝션) 에 대해서")
    print("<================================================>")
    print("\n")
    
    
    print(" \033[33m메인메뉴로 돌아가고 싶다면 0 을 입력해주세요 \033[0m")
    try :
        choiceMenu = int(input("\n번호 선택 : "))
        if choiceMenu == 1:
            # 1번 XSS
            num1()
        elif choiceMenu == 2:
            # 2번 SQLi
            num2()
        elif choiceMenu == 0:
            #0 프로그램 종료
            print("\n메인메뉴로 돌아갑니다.\n")
            break
        else:
            print("\n잘못 입력했습니다.\n")
            time.sleep(1)
    except ValueError:
        print("잘못 입력하였습니다.\n")
