from stuConn import *
# db 연결
conn = connections()


while True:
    print("[ 학생 성적 프로그램 ]")
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("0. 프로그램 종료")
    print("-"*20)
    choice = int(input("원하는 번호를 입력하세요.  "))