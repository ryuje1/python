# 파일 읽어오기
# 1. open()  2. f.read()  3. f.close()
# r : 읽기, w : 쓰기, a : 이어쓰기

with open("py0404/stu.txt", "r", encoding="utf8") as f:
    students = []
    # 1줄이면 그냥 실행, 여러줄이면 반복문 실행
    while True:
        data = f.readline()     # 1줄 읽어옴
        if not data: break      # 없으면 종료. 꼭 써주기
        # data : 1, 홍길동, 60, 100, 100, 260, 86.66666666666667, 3\n 의 형태
        # strip() : 공백제거, split(",") : 쉼표 기준으로 분리
        # \n도 문자로 인식해서 strip()을 통해 제거
        s = data.strip().split(",")
        # students = [ {"no":1, "name":name, ....} ] 모양으로 만드는 과정
        # txt => 다 문자열로 추출, 숫자의 경우 int 타입으로 변경 필요
        students.append({ "no":int(s[0]), "name":s[1], "kor":int(s[2]), "eng":int(s[3]), "math":int(s[4]), "total":int(s[5]), "avg":float(s[6]), "rank":int(s[7]) })
        
print(students)