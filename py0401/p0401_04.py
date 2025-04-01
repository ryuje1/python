students = [[1, "홍길동", 100, 100, 100, 300, 100.0, 1],
            [2, "유관순", 100, 100, 99, 299, 99.67, 2],
            [3, "이순신", 100, 100, 99, 299, 99.67, 2]]
# students = list()   # list() 다차원 리스트. [] 해놔도 상관X
# student = []        # [] 1차원 리스트
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

    # 학생 성적 입력
    if choice == 1:
        no = count
        name = input(f"{no}번 학생 이름을 입력하세요.  (0. 이전 화면 이동)   ")
        # 이전화면 이동 로직 구현
        
        kor = int(input("국어 점수를 입력하세요.  "))
        eng = int(input("영어 점수를 입력하세요.  "))
        mat = int(input("수학 점수를 입력하세요.  "))
        total = kor + eng + mat
        avg = total / 3
        rank = 0
        students.append([no, name, kor, eng, mat, total, avg, rank])
        
        count = count + 1
        
        print(f"{no}번 {name} 학생 성적이 등록되었습니다.")
        print()     # 등록 후 빠져나옴
        
    # 학생 성적 출력
    elif choice == 2:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))  # *title => 위에서 선언한 title 항목이 각각 분해되어 입력됨. 파이썬만 가능
        print("-"*60)
        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*s))
            
    # 학생 성적 수정
    elif choice == 3:
        print("[ 학생 성적 수정 ]")
        name = input("수정하려는 학생 이름을 입력하세요.  ")
        temp = 0    # 찾지 못했을 경우 사용하기 위해 쓰는 변수. 임시적으로 사용
        for i, s in enumerate(students):
            if name in s: # 있을 경우
                temp = 1
                print(f"{name} 학생을 찾았습니다.")
                print()
                print("[ 수정하려는 과목 선택]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                print("-"*20)
                choice = int(input("원하는 번호를 입력하세요.  "))
                if choice == 1:     # 국어 성적 수정
                    print("[ 국어 성적 수정 ]")
                    print(f"현재 국어 점수 : {s[2]}")
                    s[2] = int(input("변경할 국어 점수 :  "))
                    s[5] = s[2] + s[3] + s[4]   # 합계_수정
                    s[6] = s[5] / 3             # 평균_수정
                    print(f"{name} 학생 성적이 수정되었습니다. ")
                elif choice == 2:   # 영어 성적 수정
                    print("[ 영어 성적 수정 ]")
                    print(f"현재 영어 점수 : {s[3]}")
                    s[3] = int(input("변경할 국어 점수 :  "))
                    s[5] = s[2] + s[3] + s[4]   # 합계_수정
                    s[6] = s[5] / 3             # 평균_수정
                    print(f"{name} 학생 성적이 수정되었습니다. ")
                else:               # 수학 성적 수정
                    print("[ 수학 성적 수정 ]")
                    print(f"현재 수학 점수 : {s[4]}")
                    s[4] = int(input("변경할 수학 점수 :  "))
                    s[5] = s[2] + s[3] + s[4]   # 합계_수정
                    s[6] = s[5] / 3             # 평균_수정
                    print(f"{name} 학생 성적이 수정되었습니다. ")
                break
                
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력하세요~~~~")
        
        
    # 학생 성적 삭제    
    elif choice == 4:
        print("[ 학생 성적 삭제 ]")
        name = input("삭제할 학생 이름을 입력하세요.  ")
        temp = 0    # 찾았을때 1로 변경, 못찾으면 0 => 조건문 실행
        for i, s in enumerate(students):
            if name in s:   # 있을 경우
                temp = 1
                print(f"{name} 학생을 찾았습니다.")
                choice = int(input(f"{name} 학생 성적을 삭제할까요?  (0. 취소, 1.삭제)  "))     # int 타입으로 변경하지 않으려면 if choice == "1": 하면 됨
                if choice == 1:
                    print(f"{name} 학생 성적을 삭제했습니다.")
                    # 삭제 방법 : del - index() / pop() - 마지막 순번 삭제 / remove() - 해당 데이터를 가지고 삭제 / clear() - 모두 삭제
                    del students[i]
                else:
                    print(f"{name} 학생 성적 삭제를 취소했습니다.")
                break   # if문이 아니라 반복문 for문을 중지.

        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 실행하세요~~~~")
        print()
        
    elif choice == 0:
        print("프로그램 종료")
        break 
