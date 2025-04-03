# p0403_02.py 연습

# import stu_func        # stu_func 파일과 p0403_02 파일이 연결
# import stu_func as stu   # 별칭 사용. stu_func 대신 stu 사용
# from stu_func import stu_print, stu_input, stu_output     # 각각 함수명. 함수 가져옴
from stu_func import *   # 모든 함수를 가져옴 => stu. 안붙여도 실행됨
import random


students = [{"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100.0, "rank":1},
            {"no":2, "name":"유관순", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2},
            {"no":3, "name":"이순신", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2}]

count = 4
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

while True:
    print("[ 학생 성적 프로그램 ]")
    print("-"*60)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 등수 처리")
    print("0. 프로그램 종료")
    choice = int(input("원하는 프로그램 번호를 입력하세요.  "))

    # 학생 성적 입력
    if choice == 1:
        no = count
        name = input(f"{no}번 학생 이름을 입력해주세요.  ")
        kor = int(input("국어 성적을 입력해주세요.  "))
        eng = int(input("영어 성적을 입력해주세요.  "))
        math = int(input("수학 성적을 입력해주세요.  "))
        total = kor + eng + math
        avg = total / 3
        rank = 0
        
        students.append({'no':no, 'name':name, 'kor':kor, 'eng':eng, 'math':math, 'total':total, 'avg':avg, 'rank':rank})
        
        print(f"{name} 학생 성적 입력했습니다.")
        
        count += 1
    
    # 학생 성적 출력
    elif choice == 2:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*60)
        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}\t".format(s['no'], s['name'], s['kor'], s['eng'], s['math'], s['total'], s['avg'], s['rank']))
        
    # 학생 성적 수정
    elif choice == 3:
        print("[ 학생 성적 수정 ]")
        temp = 0
        name = input("수정할 학생 이름을 입력해주세요.  ")
        for s in students:
            if name == s['name']:
                temp = 1
                print(f"{name} 학생을 찾았습니다.")

        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요.")
            break
    
    # 등수 처리
    elif choice == 4:
        pass
    
    # 프로그램 종료
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break