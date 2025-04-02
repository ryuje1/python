# 10_성적딕셔너리 연습

students = [{"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100.0, "rank":1},
            {"no":2, "name":"유관순", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2},
            {"no":3, "name":"이순신", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2}]

count = 4
title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]

while True:
    print("   "*6, end="")
    print("[ 학생 성적 프로그램 ]")
    print("-"*60)

    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("0. 프로그램 종료")
    choice = int(input("원하는 프로그램 번호를 입력하세요.  "))

    # 학생 성적 입력
    if choice == 1:
        while True:
            print("[ 학생 성적 입력 ]") 
            no = count
            name = input("{}번 학생 이름을 입력해주세요.  (0. 이전화면)  ".format(no))
            if name == "0": break
            # kor = int(input("국어 성적을 입력해주세요.  "))
            # eng = int(input("영어 성적을 입력해주세요.  "))
            # math = int(input("수학 성적을 입력해주세요.  "))
            
            # for문으로 입력받기
            score = [0]*3
            for i in range(3):
                score[i] = int(input("{} 점수를 입력하세요.  ".format(title[i+2])))
            total = score[0] + score[1] + score[2]
            
            # total = kor + eng + math      # kor, eng, math 로 입력 받았을 때
            avg = total / 3
            rank = 0
        
            # append 자꾸 까먹..
            # students.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg, "rank":rank})          # 각각 입력 받았을때
            students.append({"no":no, "name":name, "kor":score[0], "eng":score[1], "math":score[2], "total":total, "avg":avg, "rank":rank})     # for문 일때
            count += 1      # 자꾸 까먹..
            
            print("{} 학생 성적 입력 완료했습니다.".format(name))
            print()
        
        
    # 학생 성적 출력
    elif choice == 2:
        print("[ 학생 성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        
        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s['no'], s['name'], s['kor'], s['eng'], s['math'], s['total'], s['avg'], s['rank']))

    # 프로그램 종료
    elif choice == 0:
        print("프로그램 종료")
        print()
        break