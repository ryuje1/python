while True:
    print("[ 프로그램 구현 ]")
    print("-"*20)
    print("1. 숫자 맞추기")
    print("2. 로또 맞추기")
    print("3. 학생 성적 프로그램")
    print("0. 종료")
    print("-"*20)
    choice = int(input("원하는 번호를 입력하세요.  "))
    
    if choice == 1: print("[ 숫자 맞추기 프로그램 ]")
    elif choice == 2: print("[ 로또 맞추기 프로그램 ]")
    elif choice == 3: print("[ 학생 성적 프로그램 ]")
    elif choice == 0: 
        print("[ 프로그램 종료 ]")
        break
    # **숫자 맞추기, 로또 맞추기, 학생 성적 프로그램은 외우기**    

# while True:
#     num = int(input("숫자를 입력하세요.  "))    # 여기까지만 하면 무한반복
#     if num == 0:
#         break   # 반복종료