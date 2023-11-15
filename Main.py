import sys
import subprocess

def num1():
    #취약점 진단 기능
    subprocess.call("Python vulnerablity analystic.py", shell=True)

def num2():
    #도구 프로그램 사용법
    subprocess.call("Python vulnerablity tool explain.py", shell=True)

def num3():
    #팀 소개 및 개발배경
    subprocess.call("Python team explain.py", shell=True)

def num4():
    #선택지 설명
    subprocess.call("Python select number explain.py", shell=True)

def num5():
    #기타
    subprocess.call("Python etc.py", shell=True)




while True:

    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃                                                                     ┃")
    print("┃       __   __         _____          __            ______           ┃")
    print("┃      /\ \ /\ \       /\  __`\       /\ \          /\__  _\          ┃")
    print("┃      \ `\`\/'/'      \ \ \/\ \      \ \ \         \/_/\ \/          ┃")
    print("┃       `\/ > <         \ \ \ \ \      \ \ \  __       \ \ \          ┃")
    print("┃          \/'/\`\       \ \ \\\'\\ \      \ \ \L\ \       \_\ \__       ┃")
    print("┃          /\_\\\ \_\      \ \___\_\      \ \____/        /\_____\     ┃")
    print("┃          \/_/ \/_/       \/__//_/       \/___/         \/_____/     ┃")
    print("┃                                                                     ┃")
    print("┃                                                                     ┃")
    print("┃                                        지금 졸작에 잠이오냐? TEAM   ┃")
    print("┃                                                                     ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("                         * 주의 사항 *                        ")
    print("    해당 도구는 취약점 진단 도구로 허가된 사용자만 사용이 가능합니다. ")
    print("    또한, 허가받은 URL을 제외한 다른 URL에                       ")
    print("    해당 도구 사용시 법적인 책임은 사용자에게 있습니다.           ")
    print("======================================================================")




    print("                                                             ")
    print("     1. 취약점 진단 시작                                      ")
    print("     2. 도구 프로그램 사용법                                   ")
    print("     3. 팀 소개 및 개발배경                                   ")
    print("     4. 보기 설명                                            ")
    print("     5. 기타                                                 ")
    print("     0. 프로그램 종료                                         ")

    try :
        choiceMenu = int(input("\n번호 선택 : "))
        if choiceMenu == 1:
            #1번 메뉴 이동
            print("\n취약점 진단을 시작합니다.\n")
        elif choiceMenu == 2:
            #2번 메뉴 이동
            print("\n도구 프로그램 사용법을 설명합니다.\n")
        elif choiceMenu == 3:
            #3번 메뉴 이동
            print("\n팀 소개 및 개발배경을 설명합니다.\n")
        elif choiceMenu == 4:
            #4번 메뉴 이동
            print("\n보기에 대한 설명을 시작합니다.\n")
        elif choiceMenu == 5:
            #5번 메뉴 이동
            print("\n기타\n")
        elif choiceMenu == 0:
            #0 프로그램 종료
            print("\n프로그램을 종료합니다.\n")
            break
        else:
            print("\n잘못된 번호를 입력했습니다.\n")

    except ValueError :
        print("\n숫자를 입력해주세요.\n")

