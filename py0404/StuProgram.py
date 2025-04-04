# import stu_func        # stu_func 파일과 p0403_02 파일이 연결
# import stu_func as stu   # 별칭 사용. stu_func 대신 stu 사용
# from stu_func import stu_print, stu_input, stu_output     # 각각 함수명. 함수 가져옴
from StuFunc import *   # 모든 함수를 가져옴 => stu. 안붙여도 실행됨
import random
students = []

### 파일 불러오기
# stu.txt 파일에서 데이터를 읽어와 students = [] 데이터 입력시킴
with open("py0404/stu.txt", "r", encoding="utf-8") as f:
    while True:                         # 여러 줄일때 반복문 적용
        line = f.readline()             # 1줄 읽어오기
        if not line: break              # 문자열이 없을때 종료
        s = line.strip().split(",")     # 1줄 문자열을 쉼표 기준으로 분리
        students.append({"no":int(s[0]), "name":s[1], "kor":int(s[2]), "eng":int(s[3]), "math":int(s[4]), "total":int(s[5]), "avg":float(s[6]), "rank":int(s[7])})


    



count = 4   # 1부터 시작해야하는데 students 에 학생이 3명 있어서 4부터 시작
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
choice = 0

# 학생 점수 수정 함수 선언
def stu_mod():
    sub_list = ['', 'kor', 'eng', 'math']   # choice를 맞추기 위해서 0번째에 공백 값
    if choice == 1:     # 국어 성적 수정
        pre_score = s[sub_list[choice]]
        print(f"현재 {title[choice+1]} 점수 : {pre_score}")
        s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]} 점수를 입력해주세요.  "))
        s['total'] = s['kor'] + s['eng'] + s['math']
        s['avg'] = s['total'] / 3
        print("변경 전 {}점을 변경 후 {}점으로 수정했습니다.".format(pre_score, s[sub_list[choice]]))


while True:
    # 화면 출력 부분
    choice = stu_print()        # stu_func 파일의 stu_print() 함수 호출

    # 학생 성적 입력
    if choice == 1:
        count = stu_input(count, students)     # count, students를 매개변수로 넘겨줌
    
    # 학생 성적 출력
    elif choice == 2:
        stu_output(title, students)
    
    # 학생 성적 수정
    elif choice == 3:
        print("[ 학생 성적 수정 ]")
        temp = 0    # 찾지 못했을 경우. 데이터베이스에는 true / false가 없어서 0 / 1 사용
        name = input("수정할 학생 이름을 입력해주세요.  ")
        
        for s in students:
            if name in s['name']:   # if s['name] == name: 과 동일
                temp = 1
                print(f"{name} 학생을 찾았습니다. 과목을 수정합니다.")
                print("[ 수정 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
                choice = int(input("수정할 과목에 맞는 숫자를 입력해주세요.  "))
                
                sub_list = ['', 'kor', 'eng', 'math']   # choice를 맞추기 위해서 0번째에 공백 값
                if choice == 1:     # 국어 성적 수정
                    pre_score = s[sub_list[choice]]
                    print(f"현재 {title[choice+1]} 점수 : {pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]} 점수를 입력해주세요.  "))
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                    print("변경 전 {}점을 변경 후 {}점으로 수정했습니다.".format(pre_score, s[sub_list[choice]]))
                elif choice == 2:   # 영어 성적 수정
                    pre_score = s[sub_list[choice]]
                    print(f"현재 {title[choice+1]} 점수 : {pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]} 점수를 입력해주세요.  "))
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                    print("변경 전 {}점을 변경 후 {}점으로 수정했습니다.".format(pre_score, s[sub_list[choice]]))
                elif choice == 3:   # 수학 성적 수정
                    pre_score = s[sub_list[choice]]
                    print(f"현재 {title[choice+1]} 점수 : {pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]} 점수를 입력해주세요.  "))
                    s['total'] = s['kor'] + s['eng'] + s['math']
                    s['avg'] = s['total'] / 3
                    print("변경 전 {}점을 변경 후 {}점으로 수정했습니다.".format(pre_score, s[sub_list[choice]]))

        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요.  ")
            
        print()
        
    # 등수 처리
    elif choice == 4:
        stu_rank(students)
        
    # 학생 성적 정렬
    elif choice == 5:
        students2 = [*students]     # 복사
        print("[ 학생 성적 정렬 ]")
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("6. 번호 역순정렬")
        print("0. 이전화면 이동")
        print("-"*60)
        choice = int(input("원하는 번호를 입력하세요.  "))
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
            students2.sort(key=lambda x:x['no'], reverse=True)
        elif choice == 0: continue
        
        stu_output(title, students2)
        
    # 학생 성적 삭제
    elif choice == 6:
        print("[ 학생 성적 삭제 ]")
        name = input("삭제하고자 하는 학생의 이름을 입력해주세요.  ")
        temp = 0
        for i, s in enumerate(students):
            if name in s['name']:
                temp = 1
                print(f"{s['no']}번 {s['name']} 학생을 찾았습니다.")
                answer = input("학생 성적을 삭제할까요? (* 삭제 시 복구 불가)")
                if answer == "y": del students[i]
                print(f"{name} 학생의 성적을 삭제했습니다.")
                print()
                break
                
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요.")
            print()
        
    # 학생 성적 저장
    elif choice == 7:
        print("[ 학생 성적 저장 ]")
        with open("py0404/stu.txt", "w", encoding="utf-8") as f:
            for s in students:
                # 1, 홍길동, 100, 100, 100, 300, 100.0, 1 형태를 만듦
                line = f"{s['no']}, {s['name']}, {s['kor']}, {s['eng']}, {s['math']}, {s['total']}, {s['avg']}, {s['rank']}\n"
                f.write(line)
        print("파일이 저장되었습니다.")
        print()
        
    # 프로그램 종료
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        print()
        break