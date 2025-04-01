## 학생 성적 프로그램 연습

students = [[1, "홍길동", 100, 100, 100, 300, 100.0, 1],
            [2, "유관순", 100, 100, 99, 299, 99.67, 2],
            [3, "이순신", 100, 100, 99, 299, 99.67, 2]]
count = 4           # 학생 번호 생성
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

# 무한반복 while문
while True:
    # 화면 출력
    print("-"*30)
    print(" "*3, end="")
    print("[ 학생 성적 프로그램 ]")
    print("-"*30)
    
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("5. 학생 성적 정렬")
    print("6. 학생 성적 검색")
    print("7. 등수 처리")
    print("0. 프로그램 종료")
    print("-"*30)
    
    choice = int(input("원하는 번호를 입력해주세요.  "))
    
    
    if choice == 1:     # 학생 성적 입력
        no = count  # 번호
        name = input("학생 이름을 입력해주세요.  ")
        kor = int(input("국어 성적을 입력해주세요.  "))
        eng = int(input("영어 성적을 입력해주세요.  "))
        mat = int(input("수학 성적을 입력해주세요.  "))
        total = kor + eng + mat
        avg = total / 3
        rank = 0
        
        students.append([no, name, kor, eng, mat, total, avg, rank])    # append 리스트 할때는 ([리스트 값]) 형식으로 넣어야 함
        count += 1
        
        print(f"{no}번 {name} 학생 성적 입력 완료") # 입력완료 확인 메시지 출력
        print() # if문 빠져나옴
            
    elif choice == 2:   # 학생 성적 출력
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))  # 타이틀부터 출력   *는 전개연산자. 각각 분해해서 값을 넣어줌
        print("-"*55)
        for s in students:      # 각 학생마다 타이틀 항목에 맞는 값 출력
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*s)) 
        
    elif choice == 3:   # 학생 성적 수정
        print("[ 학생 성적 수정 ]")
        # 이름을 입력받고 temp 설정
        name = input("수정할 학생 이름을 입력해주세요.  ")
        temp = 0
        # 학생마다 반복
        for i, s in enumerate(students):    # s[i]
            if name in s:    # 있을 경우
                temp = 1
                print(f"{name} 학생을 찾았습니다.")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                choice = int(input("수정할 과목에 맞는 번호를 입력하세요.  "))
                if choice == 1:     # 국어 성적 수정
                    print("[ 국어 성적 수정 ]")
                    print("현재 국어 성적 : {}".format(s[2]))
                    s[2] = int(input("수정 점수 입력 :  "))
                    s[5] = s[2] + s[3] + s[4]
                    s[6] = s[5] / 3
                    print(f"{name} 학생 성적 수정 완료")
                elif choice == 2:   # 영어 성적 수정
                    print("[ 영어 성적 수정 ]")
                    print("현재 영어 성적 : {}".format(s[3]))
                    s[3] = int(input("수정 점수 입력 :  "))
                    s[5] = s[2] + s[3] + s[4]
                    s[6] = s[5] / 3
                    print(f"{name} 학생 성적 수정 완료")
                else:               # 수학 성적 수정
                    print("[ 수학 성적 수정 ]")
                    print("현재 수학 성적 : {}".format(s[4]))
                    s[4] = int(input("수정 점수 입력 :  "))
                    s[5] = s[2] + s[3] + s[4]
                    s[6] = s[5] / 3
                    print(f"{name} 학생 성적 수정 완료")
                break
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요~~")
    elif choice == 4:   # 학생 성적 삭제
        print("[ 학생 성적 삭제 ]")
        name = input("삭제할 학생 이름을 입력해주세요.  ")
        temp = 0
        for i, s in enumerate(students):
            if name in s:
                temp = 1
                print(f"{name} 학생을 찾았습니다.")
                choice = int(input("삭제하시겠습니까?   (1. 삭제 0. 취소)  "))
                if choice == 1:
                    del students[i]
                    print(f"{name} 학생 성적 삭제 완료")
                else:
                    print("{} 학생 성적 삭제를 취소합니다.".format(NameError))
                break
        if temp == 0:
            print("{} 학생을 찾지 못했습니다. 다시 입력해주세요~~".format(name))
        print()
        
    elif choice == 0:   # 프로그램 종료
        print("프로그램 종료")
        break 