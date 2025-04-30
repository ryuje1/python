### 학생성적 프로그램
### 진행하세요
students = []
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
count = 1

# ---------------------------------------------------------------------------------------------------------------------------- 

# 기본 화면 출력
def menu():
    print("-"*60)
    print("[ 학생성적 프로그램 ]")
    print("-"*60)

    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("5. 등수처리")
    print("6. 학생 성적 정렬")
    choice = int(input("번호를 입력하세요.  (0. 프로그램 종료)  "))
    return choice

# 성적 입력
def input_score(count):
    print("[ 학생 성적 입력 ]")
    no = count
    name = input(f"{no}번 학생 이름을 입력하세요.  ")
    kor = int(input("국어 성적을 입력하세요.  "))
    eng = int(input("영어 성적을 입력하세요.  "))
    math = int(input("수학 성적을 입력하세요.  "))
    total = kor+eng+math
    avg = total/3
    rank = 0
    
    students.append({'no':no, 'name':name, 'kor':kor, 'eng':eng, 'math':math, 'total':total, 'avg':avg, 'rank':rank})
    
    print(f"{name} 학생 성적이 입력되었습니다.")
    print()
    
    count += 1
    return count

# 성적 출력
def output_score():
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in students:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()
    

# 성적 수정
def modify_score():
    while True:
        print("[ 학생 성적 수정 ]")
        name = input("수정할 학생 이름을 입력하세요.  (0. 이전화면 이동) ")
        if name == "0": break
        temp = 0
        
        sub_score = ['', 'kor', 'eng', 'math']
        
        for s in students:
            if name in s['name']:
                print(f"{name} 학생을 찾았습니다.")
                temp = 1
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                choice = int(input("수정할 과목에 맞는 번호를 입력하세요.  "))
                
                if(choice == 1):
                    print(f"{title[choice+1]} 성적 수정")
                    pre_kor = s[sub_score[choice]]
                    s[sub_score[choice]] = int(input("점수를 입력하세요.  "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"{name} 학생의 {title[choice+1]} 성적이 수정되었습니다. {pre_kor}점 -> {s[sub_score[choice]]}점")
                elif(choice == 2):
                    print(f"{title[choice+1]} 성적 수정")
                    pre_eng = s[sub_score[choice]]
                    s[sub_score[choice]] = int(input("점수를 입력하세요.  "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"{name} 학생의 {title[choice+1]} 성적이 수정되었습니다. {pre_eng}점 -> {s[sub_score[choice]]}점")
                else:
                    print(f"{title[choice+1]} 성적 수정")
                    pre_math = s[sub_score[choice]]
                    s[sub_score[choice]] = int(input("점수를 입력하세요.  "))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total']/3
                    print(f"{name} 학생의 {title[choice+1]} 성적이 수정되었습니다. {pre_math}점 -> {s[sub_score[choice]]}점")
        
        if(temp==0):        
            print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요.")
            print()
            break


# 성적 삭제
def del_score():
    print("[ 학생 성적 삭제 ]")
    name = input("삭제할 학생의 이름을 입력하세요.  ")
    temp = 0
    
    for i, s in enumerate(students):
        if name in s['name']:
            temp = 1
            print(f"{name} 학생을 찾았습니다.")
            answer = input("정말 삭제하시겠습니까?  (y. 삭제 / n. 취소)")
            if answer == "y":
                del students[i]
                print(f"{name} 학생의 성적을 삭제했습니다.")
                print()
            else:
                print("취소했습니다.")
                break
    
    if temp == 0:
        print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요.")
        

# 등수처리
def rank_score():
    print("[ 등수처리 ]")
    for s in students:
        num = 1
        for ss in students:
            if (s['total']<ss['total']):
                num += 1
        s['rank']=num
    print("등수 처리를 완료했습니다.")
    print()
    
 
# 성적 정렬
def sort_score():
    students2 = [*students]
    print("[ 학생 성적 정렬 ]")
    print("1. 이름 순차정렬")
    print("2. 이름 역순정렬")
    print("3. 번호 순차정렬")
    print("4. 번호 역순정렬")
    print("5. 합계 순차정렬")
    print("6. 합계 역순정렬")
    choice = int(input("원하는 번호를 입력하세요.  "))
    
    if(choice==1): students2.sort(key=lambda x:x['name'])
    elif(choice==2): students2.sort(key=lambda x:x['name'], reverse=True)
    elif(choice==3): students2.sort(key=lambda x:x['no'])
    elif(choice==4): students2.sort(key=lambda x:x['no'], reverse=True)
    elif(choice==5): students2.sort(key=lambda x:x['total'])
    elif(choice==6): students2.sort(key=lambda x:x['total'], reverse=True)
    
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    for s in students2:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")   
    
# ----------------------------------------------------------------------------------------------------------------------------  
    

while True:
    choice = menu()

    if(choice == 1): 
        count = input_score(count)

    elif(choice == 2):
        output_score()

    elif(choice == 3):
        modify_score()
        
        # print("[ 학생 성적 수정 ]")
        # name = input("수정할 학생 이름을 입력하세요.  (0. 이전화면 이동) ")
        # if name == "0": break
        # temp = 0
        
        # for s in students:
        #     if name in s['name']:
        #         print(f"{name} 학생을 찾았습니다.")
        #         temp = 1
        #         print("1. 국어")
        #         print("2. 영어")
        #         print("3. 수학")
        #         choice = int(input("수정할 과목에 맞는 번호를 입력하세요.  "))
                
        #         if(choice == 1):
        #             print("국어 성적 수정")
        #             s['kor'] = int(input("점수를 입력하세요.  "))
        #             s['total'] = s['kor']+s['eng']+s['math']
        #             s['avg'] = s['total']/3
        #             print(f"{name} 학생의 국어 성적이 수정되었습니다.")
        #         elif(choice == 2):
        #             print("영어 성적 수정")
        #             s['eng'] = int(input("점수를 입력하세요.  "))
        #             s['total'] = s['kor']+s['eng']+s['math']
        #             s['avg'] = s['total']/3
        #             print(f"{name} 학생의 영어 성적이 수정되었습니다.")
        #         else:
        #             print("수학 성적 수정")
        #             s['math'] = int(input("점수를 입력하세요.  "))
        #             s['total'] = s['kor']+s['eng']+s['math']
        #             s['avg'] = s['total']/3
        #             print(f"{name} 학생의 수학 성적이 수정되었습니다.")
        
        # if(temp==0):        
        #     print(f"{name} 학생을 찾지 못했습니다. 다시 입력해주세요.")
        #     print()
        #     break
        
    elif(choice == 4):
        del_score()
    
    elif(choice == 5):
        rank_score()
            
    elif(choice == 6):
        sort_score()
       
    else:
        print("프로그램 종료")
        print()
        break