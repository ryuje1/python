from stuFunc import *

# conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe') -> 바로 해도 되는데 예외처리 권장
# conn = connections()
# cursor = conn.cursor()

while True:
    print("[ 학생 성적 프로그램 ]")
    print("-"*20)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 검색")
    print("4. 학생 성적 정렬")
    print("5. 학생 성적 아이디, 전화번호 출력")
    print("8. 등수 처리")
    print("9. 등급 처리")
    print("0. 프로그램 종료")
    print("-"*20)
    choice = input("원하는 프로그램 번호를 입력하세요  ")
    
    if choice == "1":   # 학생 성적 입력
       stuInsert()
        
    elif choice == "2": # 학생 성적 출력
        stuAllSelect()
    
    elif choice == "3": # 학생 성적 검색
        stuSearch()
    
    elif choice == "4": # 학생 성적 정렬
        stuSort()
    
    elif choice == "5": # 학생 성적 전화번호 출력
        pass
        ## member 테이블의 id, phone 포함 stuscore 조인
        conn = connections()
        cursor = conn.cursor()
        
        sql = "select id, phone, b.* from member a, stuscore b where a.no = b.sno"
        cursor.execute(sql)
        
        rows = cursor.fetchall()
        
        for r in rows:
            print(r)
        
        cursor.close()
        conn.close()

    elif choice == "8": # 등수 처리
        rankUpdate()
        
    elif choice == "9": # 등급 처리
        gradeUpdate()

    else:
        print("프로그램을 종료합니다.")
        break



# ### update
# sql = "update stuscore2 set rank = 0"
# cursor.execute(sql)
# conn.commit()


# ### select
# sql = "select * from stuscore2"
# cursor.execute(sql)

# rows = cursor.fetchall()
# for r in rows:
#     print(r)
    
# conn.close()
    
# print("종료")