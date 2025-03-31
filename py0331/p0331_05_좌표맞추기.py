## 5x5 2차원 리스트에 랜덤으로 1-25까지의 숫자 넣기    **중요 외우기~~~~
# 1차원 리스트 생성
# 1차원 리스트 랜덤으로 섞기
# 2차원 리스트 생성
# 2차원 리스트에 1차원 랜덤번호 넣기

import random
# 1차원 리스트 생성 후 랜덤 섞기
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

# 2차원 리스트 생성 후 1차원 리스트 값을 넣기
a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j] # [5*i+j] => 0, 1, 2, 3, 4... 24까지 들어가는 공식! 외우기

# 2차원 형태 출력 부분 전체 => while문 안으로 넣기
while True:
    # 5x5 2차원 형태로 출력 (1차원은 for문 1번 사용, 2차원은 for문 2번 사용, 3차원은 for문 3번 사용)
    print("\t [ 좌표 맞추기 프로그램 ]")
    print("-"*45)

    print("*  |",end="\t")           # 맨 위 좌표 (X좌표) 0 1 2 3 4 => 1번만 나와야하니까 for문 안에 작성X
    for i in range(5):
        print(i, end="\t")
    print()
    print("-"*45)
    for i in range(5):
        print(f"{i}  |", end="\t")   # 맨 왼쪽 좌표 (Y좌표) 0 1 2 3 4
        for j in range(5):
            print(a_list[i][j], end="\t")
            # print("{:02d}".format(a_list[i][j]), end="\t") => 에러
        print()     # 5개 출력 후 줄바꿈

    print("-"*45)

    # 입력 부분
    num1 = int(input("X 좌표 :  "))
    if num1 < 0 or num1 > 4:
        print("숫자를 잘못 입력하셨습니다. 다시 입력하세요.")
        continue
    num2 = int(input("Y 좌표 :  "))
    if num2 < 0 or num2 > 4:
        print("숫자를 잘못 입력하셨습니다. 다시 입력하세요.")
        continue

    # 좌표에 값 넣기
    a_list[num2][num1] = "X"
    print(a_list[num1][num2])