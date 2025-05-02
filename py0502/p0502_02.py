from stuConn import *
## 1. db 연결
conn = connections()


## 2. 게시판 글쓰기 
title = input("게시글 제목을 입력하세요.  ")
content = input("게시글 내용을 입력하세요.  ")


## 3. 파일첨부 등록
bname = []
count = 0
while True:
    temp = input(f"{count+1}번 첨부할 파일을 입력하세요.( 0. 종료 )  ")
    if temp == '0': break
    bname.append(temp)
    count += 1
# bfile1 = input("첨부할 파일을 입력하세요.( 1.jpg )  ")
# bfile2 = input("첨부할 파일을 입력하세요.( 2.jpg )  ")
# bfile3 = input("첨부할 파일을 입력하세요.( 3.jpg )  ")


## 4. 시퀀스 번호 생성
cursor = conn.cursor()
query = "select board_seq.nextval from dual"
cursor.execute(query)
bno = cursor.fetchone()[0]     ## bno = cursor.fetchone()[0] : 9 / bno = cursor.fetchone() : (9,) -> 리스트 형태로 넘어옴
print("시퀀스번호 생성 : ", bno)


## 5. 파일 리스트 생성
# 1개씩 저장이 아니라 여러개 저장을 하기 위해 리스트 형태로 구성
# [ [9, '1.jpg'], [9, '2.jpg'], [9, '3.jpg'] ] 형태로 저장
bfile = []
for b in bname: bfile.append([bno, b])
# bfile = [[bno, b] for b in bname]     # 리스트내포  35-36과 동일

# bfile = []
# bfile.append([bno, bfile1])
# bfile.append([bno, bfile2])
# bfile.append([bno, bfile3])


## 6. db에 게시글 저장
query = "insert into board values(:bno, :btitle, :bcontent,\
        'aaa', :bno, 0, 0, 0, sysdate)"
cursor.execute(query, bno=bno, btitle=title, bcontent=content)
conn.commit()


## 7. db에 파일 첨부 여러개 저장
query = "insert into bfile values (:1, :2)"
cursor.executemany(query, bfile)
conn.commit()
conn.close()


## 8. 프로그램 종료
print(bfile)
print("프로그램을 종료합니다.")