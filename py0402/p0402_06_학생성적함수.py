### 파일 - 저장해서 불러오기
### DB에서 불러오기


### 전역변수 선언 ###

# students => 제일 바깥이 [] 이므로 리스트 타입
students = [{"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100.0, "rank":1},
            {"no":2, "name":"유관순", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2},
            {"no":3, "name":"이순신", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2}]

count = 4           # 학생 번호 생성
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']



### 함수 부분 ###

# 학생 성적 입력 함수
def stu_input(count):
    while True:
        print("[ 학생 성적 입력 ]")
        no = count
        name = input("{}번 학생 이름을 입력해주세요.  (0. 이전화면 이동)  ".format(no))
        # 이전 화면 이동
        if name == "0" : break  # 학생 성적 입력에서 전체화면으로 이동
        
        score = [0]*3   # list 생성
        score_cal(0, score) # 국어 점수 입력, 확인
        score_cal(1, score) # 영어 점수 입력, 확인
        score_cal(2, score) # 수학 점수 입력, 확인
            
        # no, name, kor, eng, math
        # 합계, 평균 구하기
        total = score[0] + score[1] + score[2]
        avg = total / 3
        rank = 0
        
        # students 입력
        students.append({"no":no, "name":name, "kor":score[0], "eng":score[1], "math":score[2], "total":total, "avg":avg, "rank":rank})
        
        print(f"{no}번 {name} 학생 성적을 저장했습니다.")
        print()
        
        count += 1  # 학생 수 1 증가
        return count

# 국어, 영어, 수학 점수를 입력하고 확인하는 함수
def score_cal(i, score):
    while True:
        score[i] = input(f"{title[i+2]} 점수를 입력하세요.  ")
        if score[i].isdigit():
            score[i] = int(score[i])      # 숫자 변환
            if 0 <= score[i] <= 100: # 0-100 사이의 값인지 확인
                    break
            else: print("점수는 0-100 사이의 값을 입력하셔야 합니다.")
        else:
            print("숫자만 가능합니다.")
    
    
    

while True:
    print("   "*6, end="")
    print("[ 학생 성적 프로그램 ]")
    print("-"*60)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("0. 프로그램 종료")
    print("-"*60)
    choice = int(input("원하는 번호를 입력해주세요.  "))

    # 번호 선택
    if choice == 1:     # 학생 성적 입력
        count = stu_input(count)
        
    elif choice == 2:   # 학생 성적 출력
        print("[ 학생 성적 출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    
        print()
        
    elif choice == 3:   # 학생 성적 수정
        while True:
            print("[ 학생 성적 수정 ]")
            name = input("수정하려는 학생 이름을 입력하세요.  (0. 이전 화면 이동)  ")
            if name == "0": break
            temp = 0 # 찾고자 하는 학생이 있는지 없는지 확인하기 위함. 임시 변수
            
            for s in students:
                if name in s['name']:   # 수정할 학생을 찾았을 경우
                    temp = 1            # temp 1로 변경
                    print(f"{name} 학생을 찾았습니다. 성적을 수정합니다.")
                    print("[ 수정할 과목 선택 ]")
                    print("1. 국어")
                    print("2. 영어")
                    print("3. 수학")
                    print("-"*60)
                    choice = int(input("원하는 번호를 입력하세요.  "))
                    
                    if choice == 1:     # 국어 수정
                        pre_kor = s['kor']  # 이전 국어 점수를 저장
                        print("현재 국어 점수 : {}".format(pre_kor))
                        s['kor'] = int(input("변경 국어 점수 : "))
                        s['total'] = s['kor'] + s['eng'] + s['math']
                        s['avg'] = s['total'] / 3
                        print("국어 점수 : {}점을 {}점으로 수정했습니다.".format(pre_kor, s['kor']))
                    elif choice == 2:   # 영어 수정
                        pre_eng = s['eng']  # 이전 영어 점수를 저장
                        print("현재 영어 점수 : {}".format(pre_eng))
                        s['eng'] = int(input("변경 영어 점수 : "))
                        s['total'] = s['kor'] + s['eng'] + s['math']
                        s['avg'] = s['total'] / 3
                        print("영어 점수 : {}점을 {}점으로 수정했습니다.".format(pre_eng, s['eng']))
                    elif choice == 3:   # 수학 수정
                        pre_math = s['math']  # 이전 수학 점수를 저장
                        print("현재 수학 점수 : {}".format(pre_math))
                        s['math'] = int(input("변경 수학 점수 : "))
                        s['total'] = s['kor'] + s['eng'] + s['math']
                        s['avg'] = s['total'] / 3
                        print("수학 점수 : {}점을 {}점으로 수정했습니다.".format(pre_math, s['math']))
                    
                    print()
            
            if temp == 0:   # 수정할 학생을 찾지 못했을 경우
                print("{} 학생을 찾지 못했습니다. 다시 입력해주세요~~".format(name))
                print()
        
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        print()
        break