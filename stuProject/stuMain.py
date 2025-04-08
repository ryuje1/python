from stuModule import *     # = from stuModule import Student, Students
from stuFunc import *       # * => 함수, 변수 모두 가져온다는 의미


# 학생 성적 프로그램
while True:
    choice = tmenu_print()  # 상단 메뉴 부분
    
    if choice == 1:
        stu_input()     # 학생 성적 입력 함수
        
    elif choice == 2:
        stu_output()    # 학생 성적 출력 함수
        
    elif choice == 3:
        stu_modify()    # 학생 성적 수정 함수
        
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        print()
        break