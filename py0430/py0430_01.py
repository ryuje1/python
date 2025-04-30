import dbconn

print("------------db연결------------")
# db 접속
conn = dbconn.connections()                        # sql developer 프로그램 오픈과 같음
cursor = conn.cursor()                      # sql 창 오픈

name = input("검색하려는 이름을 입력하세요.  ")
name = '%'+name+'%'
query = "select employee_id, emp_name, salary from employees where emp_name like :name"
cursor.execute(query, name=name)

## employees 월급이 4000 - 6000 사이의 사번, 이름, 월급
# query = "select employee_id, emp_name, salary from employees where salary>=4000 and salary<=6000"
# cursor.execute(query)
# cursor.execute("select * from stuscore where sno>=50")    # sql구문 F9 실행
rows = cursor.fetchall()                    # 데이터를 가져옴 (튜플형태)


for r in rows:
    print(r[0], r[1], r[2])
    # print(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])

# print("학생 성적 출력")
# print(f"{"번호"}\t{"이름"}\t{"국어"}\t{"영어"}\t{"수학"}\t{"합계"}\t{"평균"}\t{"등수"}")
# print(f"{r['sno']}\t{r['name']}\t{r['kor']}\t{r['eng']}\t{r['math']}\t{r['total']}\t{r['avg']}\t{r['rank']}")


# pip install oracledb 입력해서 설치