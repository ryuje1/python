# 1. sModule.py - 2개의 class 생성
# 2. sMain.py
#    - sModule.py 사용해서 프로그램 구현
# 3. sFunc.py 함수 옮기기

from sModule import *
from sFunc import *

while True:
    choice = tmenu_print()

    if choice == 1: # 성적 입력
        stu_input()
        
    elif choice == 2: # 성적 출력
        stu_output()
            
    elif choice == 3: # 성적 수정
        print("[ 학생 성적 수정 ]")
        
        
    elif choice == 0: # 프로그램 종료
        print("[ 프로그램 종료 ]")
        print()
        break