from sModule import *

students = Students()
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

def tmenu_print():
    print("-"*60)
    print("[ 학생 성적 프로그램 ]")
    print("-"*60)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("0. 프로그램 종료")
    choice = 0
    try:
        choice = int(input("원하는 프로그램 번호를 입력하세요.  "))
    except Exception as e: print(e)
    return choice

def stu_input():
    print("[ 학생 성적 입력 ]")
    name = input(f"{Student.count}번 학생 이름을 입력해주세요.  ")
    score = [0]*3
    for i in range(len(score)):
        score[i] = int(input(f"{title[i+2]} 성적을 입력해주세요.  "))
    students.add(Student(name, score[0], score[1], score[2]))   # append 아니고 add
    print(f"{name} 학생 성적을 입력했습니다.")
    print()
    
def stu_output():
    print("[ 학생 성적 출력 ]")
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in students.students:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s.no, s.name, s.kor, s.eng, s.math, s.total, s.avg, s.rank))