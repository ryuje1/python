# 딕셔너리 생성
students = [{"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100.0, "rank":1},
            {"no":2, "name":"유관순", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2},
            {"no":3, "name":"이순신", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2}]

count = 4           # 학생 번호 생성
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']


while True:
    print("   "*6, end="")
    print("[ 학생 성적 프로그램 ]")
    print("-"*60)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("0. 프로그램 종료")
    print("-"*60)
    choice = int(input("원하는 번호를 입력해주세요.  "))
    
    # 학생 성적 입력
    if choice == 1:
        while True: # 0번 누르기 전까지 계속 학생 성적 입력하도록 반복
            print("[ 학생 성적 입력 ]")
            no = count
            name = input("{}번 학생 이름을 입력해주세요.     (0. 이전화면 이동)  ".format(no))
            if name == '0': break
            kor = int(input("국어 성적을 입력해주세요.  "))
            eng = int(input("영어 성적을 입력해주세요.  "))
            math = int(input("수학 성적을 입력해주세요.  "))
            # # 국어, 영어, 수학 성적 입력받는 for문 (컬럼이 많을때 for문 사용하면 3줄로 끝낼 수 있음)
            # score = [0]*3  # [0, 0, 0] kor, eng, math   # append 로 추가하는 것 보다 만들어놓고 추가하는 것이 속도가 좀 더 빠름
            # for i in range(3):
            #     score[i] = int(input(f"{title[i+2]} 점수를 입력하세요.  "))
            total = kor + eng + math
            avg = total / 3     # 나누기는 float 타입으로 변경됨
            rank = 0
            
            students.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg, "rank":rank})   # students에 값 추가
            
            count += 1  # 학생 번호 1 증가
            
            print("{}번 {} 학생 성적 입력 완료했습니다.".format(no, name))
            print()
    # 학생 성적 출력
    elif choice == 2:
        print("   "*7, end="")
        print("[ 학생 성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        # 딕셔너리일때 값 출력
        for s in students:
            # print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s['no'], s['name'], s['kor'], s['eng'], s['math'], s['total'], s['avg'], s['rank']))
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
    # 프로그램 종료
    elif choice == 0:
        print("[프로그램 종료]")
        print()
        break