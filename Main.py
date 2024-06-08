import sys
import subprocess
import time

'''
def num1():
    # 취약점 진단 기능
    print("\n Reflected XSS 취약점 진단을 시작합니다. \n")
    subprocess.run(["python", "XSS/main.py"])

'''
def num1():
    #취약점 진단 기능
    #subprocess.call("Python vulnerablity analystic.py", shell=True)
    subprocess.run(["python3", "vulnerablity analystic.py"])


def num2():
    #도구 프로그램 사용법
    #subprocess.call("Python vulnerablity tool explain.py", shell=True)
    subprocess.run(["python3", "vulnerablity tool explain.py"])

def num3():
    #팀 소개 및 개발배경
    #subprocess.call("Python team explain.py", shell=True)
    subprocess.run(["python3", "team explain.py"])

def num4():
    #선택지 설명
    #subprocess.call("select number explain.py", shell=True)
    subprocess.run(["python3", "select number explain.py"])

def num5():
    #대화형 인터페이스
    #subprocess.call("Python etc.py", shell=True)
    subprocess.run(["python3", "etc.py"])




while True:

                                                            

    print(r"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(r"┃                                                                     ┃")
    print(r"┃                     __  ______    _    ____                         ┃")
    print(r"┃                     \ \/ / ___|  / \  / ___|                        ┃")
    print(r"┃                      \  /\___ \ / _ \ \___ \                        ┃")
    print(r"┃                      /  \ ___) / ___ \ ___) |                       ┃")
    print(r"┃                     /_/\_\____/_/   \_\____/                        ┃")
    print(r"┃                                                            3 TEAM   ┃")
    print(r"┃                                                                     ┃")
    print(r"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("\033[38;2;255;0;0m")
    print("                         * 주의 사항 *                        ")
    print("   해당 도구는 취약점 진단 도구로 허가된 사용자만 사용이 가능합니다.")
    print("              또한, 허가받은 URL을 제외한 다른 URL에")
    print("       해당 도구 사용시 법적인 책임은 사용자에게 있습니다.\033[0m")
    print("=======================================================================")
    print("                                                           Version 0.1")

    

    print("\n")
    print("     🔍 1. 취약점 진단 시작                                    ")
    print("     ❓ 2. 도구 프로그램 사용법                                ")
    print("     🧐 3. 팀 소개 및 개발배경                                   ")
    print("     📋 4. 보기 설명                                            ")
    print("     💬 5. 어떤 취약점을 진단해야할지 모르겠어요                          ")
    print("     ❌ 0. 프로그램 종료                                         ")

    try :
        choiceMenu = int(input("\n번호 선택 : "))
        if choiceMenu == 1:
            #1번 메뉴 이동
            print("\n🔍 취약점 진단을 시작합니다.\n")
            time.sleep(1)
            num1()
        elif choiceMenu == 2:
            #2번 메뉴 이동
            print("\n❓ 도구 프로그램 사용법을 설명합니다.\n")
            time.sleep(1)
            num2()
        elif choiceMenu == 3:
            #3번 메뉴 이동
            print("\n🧐 팀 소개 및 개발배경을 설명합니다.\n")
            time.sleep(1)
            num3()
        elif choiceMenu == 4:
            #4번 메뉴 이동
            print("\n📋 보기에 대한 설명을 시작합니다.\n")
            time.sleep(1)
            num4()
        elif choiceMenu == 5:
            #5번 메뉴 이동
            print("\n💬 맞춤형 대화를 시작합니다.\n")
            time.sleep(1)
            num5()
        elif choiceMenu == 0:
            #0 프로그램 종료
            print("\n❌ 프로그램을 종료합니다.\n")
            break
        else:
            print("\n❗ 잘못된 번호를 입력했습니다.\n")
            time.sleep(1)

    except ValueError :
        print("\n❗ 숫자를 입력해주세요.\n")
        time.sleep(1)

