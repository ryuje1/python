### 학생성적 프로그램에서 1명의 학생을 등록해보세요.

from stuConn import *
conn = connections()

print("[ 학생성적 프로그램 ]")
print("1. 학생성적 입력")
print("2. 학생성적 출력")
print("0. 프로그램 종료")
print("-"*20)
choice = int(input("원하는 프로그램 번호를 입력하세요.  "))

# 학생 성적 입력
if choice == 1:
    name = input("학생 이름을 입력해주세요.  ")
    kor = int(input("국어 점수를 입력해주세요.  "))
    eng = int(input("영어 점수를 입력해주세요.  "))
    math = int(input("수학 점수를 입력해주세요.  "))
    total = kor+eng+math
    avg = total/3
    
    query = "insert into stuscore values(stuscore_seq.nextval, :name1, :kor1, :eng1, :math1, :total1, :avg, 0)"
    cursor = conn.cursor()
    cursor.execute(query, name1=name, kor1=kor, eng1=eng, math1=math, total1=total, avg1=avg)
    conn.commit()

# 학생 성적 출력
elif choice ==2:
    query = "select * from stuscore"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        print(r)


conn.close()