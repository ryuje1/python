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
            
    # elif choice == 3: # 성적 수정
        # temp = 0
        # print("[ 학생 성적 수정 ]")
        # name = input("수정할 학생 이름을 입력해주세요.  (0. 이전화면)  ")
        # if name == "0": break
        # for s in students.students:
        #     if name in s['name']:
        #         temp = 1
        #         print(f"{name} 학생을 찾았습니다.")
        #         print("[ 수정할 과목 선택 ]")
        #         print("1. 국어")
        #         print("2. 영어")
        #         print("3. 수학")
        #         choice = int(input("수정할 과목에 맞는 번호를 입력해주세요.  "))
                
        #         sub_list = ["", "국어", "영어", "수학"]
        #         if choice == 1:
        #             pre_kor = s[sub_list[]]
        # if temp == 0: 
        #     print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요.!")
        #     continue
        
    elif choice == 0: # 프로그램 종료
        print("[ 프로그램 종료 ]")
        print()
        break