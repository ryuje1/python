# 숫자 맞추기 프로그램
# p0331_07_좌표맞추기번호입력.py 참고

# 1차원 배열 1-25의 수 랜덤으로 섞기
import random
first_list = [i+1 for i in range(25)] # 1차원 배열
random.shuffle(first_list)

# 5x5 2차원 배열 생성 후 1차원 배열의 값 넣기
a_list = [[0]*5 for i in range(5)]     # 2차원 배열
for i in range(5):
    for j in range(5):
        a_list[i][j] = first_list[5*i+j]    # 0-24의 랜덤 번호 a_list에 넣기
        
while True:               
    # 5x5 2차원 형태로 출력
    print("[ 좌표 맞추기 게임 ]")
    print("-"*45)

    print("*  |", end ="\t")
    for i in range(5):
        print(i, end="\t")
    print()
    print("-"*45)

    for i in range(5):
        print(f"{i}  |", end="\t")
        for j in range(5):
            print(a_list[i][j], end="\t")
        print()
    print("-"*45)

    # 입력
    input_num = int(input("숫자를 입력하세요.  "))
    for i in range(5):
        for j in range(5):
            if input_num == a_list[i][j]:
                a_list[i][j] = "X"