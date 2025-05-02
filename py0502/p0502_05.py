### 
## board 테이블, bfile 테이블
### bfile테이블 : a1.jpg, a2.jpg 저장하시오.
## 게시글 저장 - bfile 컬럼

from stuConn import *

## 1. db연결
conn = connections()

## 게시글 작성
btitle = "파일첨부 게시글 제목입니다."
bcontent = "파일첨부 게시글 내용입니다."
query = "insert into board values (:bno, :btitle, :bcontent, 'aaa', :bno, 0, 0, 0, sysdate)"

## 2. 시퀀스번호 생성 : bno 저장
cursor = conn.cursor()
cursor.execute("select board_seq.nextval from dual")
bno = cursor.fetchone()[0]      # (15, )

## 3-1 db에 게시글 저장
cursor.execute(query, bno=bno, btitle=btitle, bcontent=bcontent)
conn.commit()

## 3. 리스트 생성  - a1.jpg, a2.jpg
## [[bno, 'a1.jpg'], [bno, 'a2.jpg']]
bfileList = []
bfileList.append([bno, 'a1.jpg'])
bfileList.append([bno, 'a2.jpg'])

## 4. db 저장
query = "insert into bfile values(:1, :2)"
cursor.executemany(query, bfileList)
conn.commit()

## 5. 프로그램 종ㄹ료
conn.close()
print("프로그램 종료")