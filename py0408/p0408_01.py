#           0      1       2      3       4      5       6       7
title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]

while True:
    print("1. 국어 입력")
    print("2. 영어 입력")
    print("3. 수학 입력")
    choice = int(input("원하는 번호를 입력하세요.  "))
    
    if choice == 1:
        print(f"[ {title[choice+1]} 성적 입력 ]")
    elif choice == 2:
        print(f"[ {title[choice+1]} 성적 입력 ]")
    elif choice == 3:
        print(f"[ {title[choice+1]} 성적 입력 ]")