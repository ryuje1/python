from stuModule import *     # = from stuModule import Student, Students

# Students 객체 선언 ------------------------------------------------------
students = Students()
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
# ------------------------------------------------------------------------

# 상단 메뉴 출력 함수 선언 -------------------------------------------------
def tmenu_print():
    print("  "*20)
    print("[ 학생 성적 처리 프로그램 ]")
    print("-"*50)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("0. 프로그램 종료")
    choice = 0
    try:
        choice = int(input("원하는 번호를 입력하세요.  "))
    except Exception as e: print(e)
    
    return choice
# ------------------------------------------------------------------------


# 학생 성적 입력 함수 선언 -------------------------------------------------
def stu_input():
    print("[ 학생 성적 입력 ]")
    name = input(f"{Student.count}번째 학생 이름을 입력해주세요.  ")
    score = [0]*3
    for i in range(len(score)):
        score[i] = int(input(f"{title[i+2]} 점수를 입력하세요.  "))
    students.add(Student(name, *score))
    print(f"{name} 학생이 등록되었습니다.")
    print()
# ------------------------------------------------------------------------


# 학생 성적 출력 함수 선언 -------------------------------------------------
def stu_output():
    print("[ 학생 성적 출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in students.students:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s.no, s.name, s.kor, s.eng, s.math, s.total, s.avg, s.rank))
# ------------------------------------------------------------------------