import oracledb

# db연결
def connections ():
    try: conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn

## 학생 성적 입력
def stuInsert():
    conn = connections()
    cursor = conn.cursor()
    
    # 이름, 국어, 영어, 수학 점수 입력 -> 합계, 평균, 등수, 등급처리
    name = input("이름을 입력해주세요.  ")
    kor = int(input("국어 성적을 입력해주세요.  "))
    eng = int(input("영어 성적을 입력해주세요.  "))
    math = int(input("수학 성적을 입력해주세요.  "))
    total = kor + eng + math
    avg = total / 3
    rank = 0
    sgrade = 'A'
    
    sql = "insert into stuscore values(stuscore_seq.nextval, :name, :kor, :eng, :math, :total, :avg, :rank, :sgrade)"
    cursor.execute(sql, name=name, kor=kor, eng=eng, math=math, total=total, avg=avg, rank=rank, sgrade=sgrade)
    conn.commit()
    
    cursor.close()
    conn.close()
    
    print("성적 입력 완료")


## 학생 전체 출력
def stuAllSelect(sql = "select * from stuscore"):
    conn = connections()
    cursor = conn.cursor()
    
    cursor.execute(sql)

    rows = cursor.fetchall()
    for r in rows:
        print(r)
    
    cursor.close()
    conn.close()
    
    
## 학생 성적 검색
def stuSearch():
    conn = connections()
    cursor = conn.cursor()
    
    search_input = input("검색하려는 학생 이름을 입력하세요.  ")
    sql = "select * from stuscore where name like '%'||:search||'%'"
    cursor.execute(sql, search=search_input)      # sql문 변수 = input변수
    
    rows = cursor.fetchall()
    
    if len(rows)>0:
        for r in rows:
            print(r)
    else:
        print(f"[{search_input}] 학생을 찾지 못했습니다. 다시 입력해주세요.")
    
    cursor.close()
    conn.close()
    
    
## 학생 성적 정렬
def stuSort():
    conn = connections()
    cursor = conn.cursor()
    
    print("[ 학생 성적 정렬 ]")
    print("1. 이름 정렬")
    print("2. 성적 정렬")
    print("3. 국어 정렬")
    print("4. 영어 정렬")
    print("5. 수학 정렬")
    print("6. 번호 정렬")
    choice = int(input("원하는 정렬 방식의 번호를 입력하세요.  "))
    
    if choice == 1: sorting('이름', 'name')
        # print("1. 이름 순차 정렬")
        # print("2. 이름 역순 정렬")
        # choice2 = int(input("원하는 정렬 번호를 입력해주세요.  "))
        # if choice2 == 1:
        #     sql = "select * from stuscore order by name"
        # else:
        #     sql = "select * from stuscore order by name desc"
        # stuAllSelect(sql)
        
    elif choice == 2: sorting('성적', 'total')
        # print("1. 성적 순차 정렬")
        # print("2. 성적 역순 정렬")
        # choice2 = int(input("원하는 정렬 번호를 입력해주세요.  "))
        # if choice2 == 1:
        #     sql = "select * from stuscore order by total"
        # else:
        #     sql = "select * from stuscore order by total desc"
        # stuAllSelect(sql)
        
    elif choice == 3: sorting('국어', 'kor')
        # print("1. 국어 순차 정렬")
        # print("2. 국어 역순 정렬")
        # choice2 = int(input("원하는 정렬 번호를 입력해주세요.  "))
        # if choice2 == 1:
        #     sql = "select * from stuscore order by kor"
        # else:
        #     sql = "select * from stuscore order by kor desc"
        # stuAllSelect(sql)
        
    elif choice == 4: sorting('영어', 'eng')
        # print("1. 영어 순차 정렬")
        # print("2. 영어 역순 정렬")
        # choice2 = int(input("원하는 정렬 번호를 입력해주세요.  "))
        # if choice2 == 1:
        #     sql = "select * from stuscore order by eng"
        # else:
        #     sql = "select * from stuscore order by eng desc"
        # stuAllSelect(sql)
        
    elif choice == 5: sorting('수학', 'math')
        # print("1. 수학 순차 정렬")
        # print("2. 수학 역순 정렬")
        # choice2 = int(input("원하는 정렬 번호를 입력해주세요.  "))
        # if choice2 == 1:
        #     sql = "select * from stuscore order by math"
        # else:
        #     sql = "select * from stuscore order by math desc"
        # stuAllSelect(sql)
    elif choice == 6: sorting('번호', 'sno')
        # print("1. 번호 순차 정렬")
        # print("2. 번호 역순 정렬")
        # choice2 = int(input("원하는 정렬 번호를 입력해주세요.  "))
        # if choice2 == 1:
        #     sql = "select * from stuscore order by sno"
        # else:
        #     sql = "select * from stuscore order by sno desc"
        # stuAllSelect(sql)
    
    cursor.close()
    conn.close()

## 순차정렬, 역순정렬
def sorting(sName, sName2):
    print(f"1. {sName} 순차 정렬")
    print(f"2. {sName} 역순 정렬")
    choice2 = int(input("원하는 정렬 번호를 입력해주세요.  "))
    if choice2 == 1:
        sql = f"select * from stuscore order by {sName2}"
    else:
        sql = f"select * from stuscore order by {sName2} desc"
    stuAllSelect(sql)

## 등수 처리 - 1, 2, 3,...
def rankUpdate():
    conn = connections()
    cursor = conn.cursor()
    
    sql = "update stuscore a set rank = (select ranks from (select sno, rank() over(order by total desc) ranks from stuscore) b where a.sno = b.sno)"
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    conn.close()
    
    print("등수 처리 완료")
    

## 등급 처리 - A, B, C, D, F
def gradeUpdate():
    conn = connections()
    cursor = conn.cursor()
    
    sql = "update stuscore a set sgrade = (select grade from (select sno, avg, grade from stuscore, scoregrade where avg between minscore and maxscore) b where a.sno = b.sno)"
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    conn.close()
    
    print("등급 처리 완료")