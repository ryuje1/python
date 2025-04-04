## 학생 성적 프로그램 전부 다 해보기
## 입력, 출력, 수정, 등수처리, 정렬, 삭제, 저장, 프로그램 종료
## 입력, 출력, 저장, 프로그램 종료 만이라도 외우기!!
import random
students = []

## 중요 외우기~~ ##
# stu.txt에서 students [] 값 넣기
with open("py0404/stu.txt", "r", encoding="utf-8") as f:
    while True:     # 여러 줄 가져올거면 반복문
        data = f.readline()     # 1줄씩 읽어옴 (1,홍길동,60,100,100,260,86.66666666666667,3)
        if not data: break
        s = data.replace(" ","").split(",")     # 공백제거, 분리해서 s에 넣음
        # {"no":1, "name":"홍길동", "kor":100, ...} 형태로 만들기
        students.append({"no":int(s[0]), "name":s[1], "kor":int(s[2]), "eng":int(s[3]), "math":int(s[4]), "total":int(s[5]), "avg":float(s[6]), "rank":int(s[7])})

title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '순위']
# count 숫자 대신 students no의 최대값 +1 로 구현
count = max(students, key=lambda x:x['no'])['no']+1

while True:
    print("   "*6, end="")
    print("[ 학생 성적 프로그램 ]")
    print("-"*60)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 등수 처리")
    print("5. 학생 성적 정렬")
    print("6. 학생 성적 삭제")
    print("7. 학생 성적 저장")
    print("0. 프로그램 종료")
    print("-"*60)
    choice = int(input("원하는 프로그램의 번호를 입력해주세요. "))

    # 학생 성적 입력
    if choice == 1:
        print("[ 학생 성적 입력 ]")
        no = count
        name = input("{}번 학생 이름을 입력해주세요.  ".format(no))
        kor = int(input("국어 성적을 입력해주세요.  "))
        eng = int(input("영어 성적을 입력해주세요.  "))
        math = int(input("수학 성적을 입력해주세요.  "))
        total = kor + eng + math
        avg = total / 3
        rank = 0
        students.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg, "rank":rank})
        count += 1
        print(f"{name} 학생 성적 입력했습니다.")
        print()
        
    # 학생 성적 출력
    elif choice == 2:
        print("[ 학생 성적 출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s['no'], s['name'], s['kor'], s['eng'], s['math'], s['total'], s['avg'], s['rank']))

    # 학생 성적 수정
    # 하다 말았음..
    elif choice == 3:
        print("[ 학생 성적 수정 ]")
        temp = 0    # 있는지 확인
        name = input("수정하고자 하는 학생 이름을 입력해주세요.  ")
        for s in students:
            if name in s['name']:
                temp = 1
                print(f"{name} 학생을 찾았습니다.")
                print("[ 수정할 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                choice = int(input("과목에 맞는 번호를 입력해주세요.  "))
                
                sub_list = ['', '']
                if choice == 1:     # 국어
                    pre_kor = s['kor']
                elif choice == 2:   # 영어
                    pass
                elif choice == 3:   # 수학
                    pass
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요. ")
            print()
            break

    # 등수 처리
    elif choice == 4:
        print("[ 등수 처리 ]")
        for s in students:
            num = 1
            for ss in students:
                if s['total'] < ss['total']:    # 등수 비교
                    num += 1                    # 등수 1 증가
            s['rank'] = num                     # 등수 입력
        print("등수 처리 완료했습니다.")
        print()

    # 학생 성적 정렬
    # .sort
    elif choice == 5:
        # 정렬 전 students2에 student 복사
        students2 = [*students]
        print("[ 학생 성적 정렬 ]")
        print("-"*60)
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("6. 번호 역순정렬")
        print("0. 이전화면 이동")
        choice = int(input("원하는 정렬 번호를 입력해주세요.  "))
        
        if choice == 1:     # 이름 순차정렬
            students2.sort(key=lambda x:x['name'])
        elif choice == 2:   # 이름 역순정렬
            students2.sort(key=lambda x:x['name'], reverse=True)
        elif choice == 3:   # 합계 순차정렬
            students2.sort(key=lambda x:x['total'])
        elif choice == 4:   # 합계 역순정렬
            students2.sort(key=lambda x:x['total'], reverse=True)
        elif choice == 5:   # 번호 순차정렬
            students2.sort(key=lambda x:x['no'])
        elif choice == 6:   # 번호 역순정렬
            students.sort(key=lambda x:x['no'], reverse=True)
        elif choice == 0:   # 이전화면 이동
            continue
        
        # 출력
        print("[ 학생 성적 출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        for s in students2:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s['no'], s['name'], s['kor'], s['eng'], s['math'], s['total'], s['avg'], s['rank']))

    # 학생 성적 삭제
    elif choice == 6:
        print("[ 학생 성적 삭제 ]")
        temp = 0
        name = input("삭제하고자 하는 학생의 이름을 입력해주세요.  ")
        for i, s in enumerate(students):
            if name in s['name']:
                temp = 1
                print(f"{s['no']}번 {s['name']} 학생을 찾았습니다.")
                answer = input("정말 삭제하시겠습니까?  (*삭제 시 복구 불가)")
                if answer == "y": del students[i]
                print(f"{name} 학생 성적을 삭제했습니다.")
                break
        
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요")
            print()
            break

    # 학생 성적 저장
    elif choice == 7:
        print("[ 학생 성적 저장 ]")
        # 파일 열고 쓰기
        with open("py0404/stu.txt", "w", encoding="utf-8") as f:
            for s in students:
                # 문자열로 만들기
                data = f"{s['no']}, {s['name']}, {s['kor']}, {s['eng']}, {s['math']}, {s['total']}, {s['avg']}, {s['rank']}\n"
                f.write(data)
        print("학생 성적 저장했습니다.")
        print()
                

    # 프로그램 종료
    else:
        print("[ 프로그램 종료 ]")
        break