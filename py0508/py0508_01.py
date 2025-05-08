import oracledb

## db 연결
def connections():
    try: conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn


while True:
    print("[ 학생 성적 프로그램 ]")
    print("-" * 30)
    print("1. 학생 전체 출력")
    print("2. 학반 별 최고 등수 출력")
    print("3. 학반 별 최하 등수 출력")
    print("4. 부서별 최고연봉 출력")
    print("5. stuscore2 학반 부여(1-10, 11-20...)")
    print("6. 회원정보 rownum 사용해서 11-20번 출력")
    print("0. 프로그램 종료")
    print("-" * 30)
    choice = int(input("원하는 번호를 입력하세요.   "))
    
    
    if choice == 1:
        title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등급', '학반']
        conn = connections()
        cursor = conn.cursor()
        
        print("학생 전체 출력")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-" * 65)
        
        sql = "select * from stuscore2"
        cursor.execute(sql)
        
        rows = cursor.fetchall()
        for r in rows:
            print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\t{r[6]}\t{r[7]}\t{r[8]}\t{r[9]}")
            # print(f"{r['sno']}\t{r['name']}\t{r['kor']}\t{r['eng']}\t{r['math']}\t{r['total']}\t{r['avg']:.2f}\t{r['rank']}\t{r['sgrade']}\t{r['sclass']}")
        print()
        
        cursor.close()
        conn.close()
    
    elif choice == 2:
        title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등급', '학반']
        conn = connections()
        cursor = conn.cursor()
        
        print("학반 별 최고 등수 출력")
        
        sql = "select * from stuscore2 a where rank in (select max(rank) from stuscore2 b where a.sclass = b.sclass group by sclass)"
        cursor.execute(sql)
        
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-" * 65)
        
        rows = cursor.fetchall()
        for r in rows:
            print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\t{r[6]}\t{r[7]}\t{r[8]}\t{r[9]}")
        
        cursor.close()
        conn.close()
    
    elif choice == 3:
        title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등급', '학반']
        conn = connections()
        cursor = conn.cursor()
        
        print("학반 별 최하 등수 출력")
        
        sql = "select * from stuscore2 a where rank in (select min(rank) from stuscore2 b where a.sclass = b.sclass group by sclass)"
        cursor.execute(sql)
        
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-" * 65)
        
        rows = cursor.fetchall()
        for r in rows:
            print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\t{r[6]}\t{r[7]}\t{r[8]}\t{r[9]}")
        
        cursor.close()
        conn.close()
    
    elif choice == 4:
        pass
    
    elif choice == 5:
        conn = connections()
        cursor = conn.cursor()
        
        sql = "update stuscore2 set sclass = \
        case \
        when sno<=10 then 1 \
        when sno<=20 then 2 \
        when sno<=30 then 3 \
        when sno<=40 then 4 \
        when sno<=50 then 5 \
        when sno<=60 then 6 \
        when sno<=70 then 7 \
        when sno<=80 then 8 \
        when sno<=90 then 9 \
        when sno<=100 then 10 \
        when sno<=110 then 11 \
        end"
        cursor.execute(sql)
        conn.commit()
        print("학반 부여 완료")
        
        cursor.close()
        conn.close()
    
    elif choice == 6:
        pass
    
    else:
        print("[ 프로그램 종료 ]")
        break