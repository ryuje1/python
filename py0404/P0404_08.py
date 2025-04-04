students = [{'no': 1, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': 3}, 
            {'no': 2, 'name': '유관순', 'kor': 100, 'eng': 80, 'math': 99, 'total': 279, 'avg': 93.0, 'rank': 2}, 
            {'no': 3, 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': 1}, 
            {'no': 4, 'name': '강감찬', 'kor': 74, 'eng': 16, 'math': 20, 'total': 110, 'avg': 36.666666666666664, 'rank': 5}, 
            {'no': 5, 'name': '김구', 'kor': 64, 'eng': 99, 'math': 80, 'total': 243, 'avg': 81.0, 'rank': 4}]

# stu.txt 파일의 문자를 읽어와서 리스트 타입으로 변경
# --------------
# 리스트 타입을 stu.txt에 저장
# 딕셔너리 형태를 -> 1, 홍길동, 60, 100, 100, 260, 86.66666666666667, 3

s = {'no': 1, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': 3}
data = f"{s['no']}, {s['name']}, {s['kor']}, {s['eng']}, {s['math']}, {s['total']}, {s['avg']}, {s['rank']}"
print(s)
print("-"*50)
print(data)

# stu.txt에  파일 저장
f = open("py0404/stu.txt", "w", encoding="utf8")
for s in students:
    data = f"{s['no']}, {s['name']}, {s['kor']}, {s['eng']}, {s['math']}, {s['total']}, {s['avg']}, {s['rank']}\n"
    f.write(data)
f.close()