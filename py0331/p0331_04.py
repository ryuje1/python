# 1-25까지 랜덤 리스트를 생성

import random
# 1. 순차적 리스트 생성
sample_list = [i+1 for i in range(25)]
# 2. 랜덤 리스트
random.shuffle(sample_list)

# 3. 5x5 차원 0 리스트 생성 
a_list = [[0]*5 for i in range(5)]

# 4. 5x5 차원 리스트에 랜덤리스트 값을 입력
for i in range(5):
    for j in range(5):
        a_list[i][j] = sample_list[5*i+j]

# 5. 5x5 출력
while True:
    print("  [ 좌표 맞추기 프로그램 ]  ")
    print("0 | ", end="")
    for i in range(5):
        print(i, end="\t")
    print()
    print("-"*40)
    for i in range(5):
        print(f"{i} | ", end="")
        for j in range(5):
            print(a_list[i][j], end="\t")
        print()

    print()
    num1 = int(input("x 좌표를 입력하세요.  "))
    num2 = int(input("y 좌표를 입력하세요.  "))

    a_list[num1][num2] = "X"