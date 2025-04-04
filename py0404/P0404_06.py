# 1. stu.txt 읽기
# 2. 리스트, 딕셔너리 타입으로 변환
# 3. students = [] 안에 넣기

# students 리스트
students = []
f = open("py0404/stu.txt", "r", encoding="utf-8")
while True:
    line = f.readline()             # 1, 홍길동, 100, 100, 100, 300, 100.0, 1
    if not line: break              # 읽은 문자가 없으면 종료
    s = line.strip().split(",")     # 문자열을 list 타입으로 변경
    students.append({"no":int(s[0]), "name":s[1], "kor":int(s[2]), "eng":int(s[3]), "math":int(s[4]), "total":int(s[5]), "avg":float(s[6]), "rank":int(s[7])})
f.close()

for s in students:
    print(s)


# students = [{"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100.0, "rank":1},
#             {"no":2, "name":"유관순", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2},
#             {"no":3, "name":"이순신", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2}]

# # stu.txt
# # 1, 홍길동, 100, 100, 100, 300, 100.0, 1
# # 2, 유관순, 100, 100, 99, 299, 99.67, 2
# # 3, 이순신, 100, 100, 99, 299, 99.67, 2

# # 1. students 리스트를 문자열로 변환
# # 2. 파일쓰기 - 문자열을 저장
# f = open("py0404/stu.txt", "w", encoding="utf-8")
# for s in students:
#     line = f"""{s['no']}, {s['name']}, {s['kor']}, {s['eng']}, {s['math']}, {s['total']}, {s['avg']}, {s['rank']}\n"""
#     f.write(line)
# f.close()

print("저장 완료")