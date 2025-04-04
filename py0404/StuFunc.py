# 모듈 : 함수의 집합
# import 모듈명 해서 모듈의 함수 호출 가능
# from 모듈명 import 함수명1, 함수명2, 함수명3...
# from 모듈명 import *

# 함수 사용 목적
# 1. 중복된 코드의 재사용
# 2. 소스의 가독성 증대



# 화면 출력 함수
def stu_print():
    print("   "*6, end="")
    print("[ 학생 성적 프로그램 ]")
    print("-"*60)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 등수 처리")
    print("5. 학생 성적 정렬")
    print("6. 학생 성적 삭제")
    print("7. 학생 성적 저장")
    print("0. 프로그램 종료")
    print("-"*60)
    choice = int(input("원하는 프로그램 숫자를 입력해주세요.  "))
    print()
    return choice


# 학생 성적 입력 함수 선언
def stu_input(count, students):
    print("[ 학생 성적 입력 ]")
    no = count
    name = input(f"{no}번 학생 이름을 입력하세요.  ")
    kor = int(input("국어 점수를 입력하세요.  "))
    eng = int(input("영어 점수를 입력하세요.  "))
    math = int(input("수학 점수를 입력하세요.  "))
    total = kor + eng + math
    avg = total / 3
    rank = 0
    students.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg, "rank":rank})
    print(f"{no}번 {name} 학생이 등록되었습니다.")
    print()
    
    count += 1
    
    return count    # count는 값 1개라 return 필요, students는 여러 개라 return 불필요


# 학생 성적 출력 함수 선언
def stu_output(title, students):
    print("   "*6, end="")
    print("[ 학생 성적 출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    
    for s in students:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s['no'], s['name'], s['kor'], s['eng'], s['math'], s['total'], s['avg'], s['rank']))
    
    print()


# 과목 점수 수정


# 학생 성적 등수 처리 함수 선언
def stu_rank(students):
    print("[ 등수 처리 ]")
    for s in students:
        num = 1
        for ss in students:
            if s['total'] < ss['total']:    # 등수 비교
                num += 1                    # 등수 1 증가
        s['rank'] = num                     # 등수 입력
    
    print("등수 처리가 완료되었습니다.")
    print()