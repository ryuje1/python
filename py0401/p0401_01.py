## 중요중요 꼭 꼭 외워두기~~~~
## 1차원, 2차원 리스트 생성 외워두기

# 1차원 리스트
import random
s_list = [i for i in range(1, 26)]  # 1차원 리스트 생성
# s_list = [i+1 for i in range(25)]   # 위와 동일. 속도 비슷
random.shuffle(s_list)
# random.random(), random.randint(), random.sample(), random.shuffle()  **알아두면 좋음
print(s_list)

# 2차원 리스트
my_list = [[0]*5 for _ in range(5)] # _ => 아무 변수도 받지 않겠다. i와 같은 의미   2차원 리스트 생성
print(my_list)

# my_list[0][1] = 1   # 값 변경

# 1차원 리스트 값을 2차원 리스트에 입력
for i in range(5):
    for j in range(5):
        my_list[i][j] = s_list[5*i+j]   # 5x+y

# 화면 출력 부분 전체 while문
while True:
    # 화면 출력
    print("  "*4, end="")
    print(" [ 좌표 맞추기 프로그램 ] ")
    print("-"*45)

    print("*  |", end="\t")     # 좌표 * 출력
    # 좌표 출력
    for i in range(5):
        print(i, end="\t")
    print()

    print("-"*45)

    # my_list 출력
    for i in range(5):
        print(f"{i}  |", end="\t")      # 왼쪽 좌표 출력
        for j in range(5):
            print(my_list[i][j], end="\t")
        print()
        
    print("-"*45)
    
    
    # X 표시 #

    # # 좌표 입력 시, X 표시
    # x = int(input("X 좌표 :  "))
    # y = int(input("Y 좌표 :  "))

    # my_list[y][x] = "X"
    
    # 숫자 입력 시, X 표시
    num = int(input("1-25번 숫자를 입력하세요.  "))
    
    # 2차원 리스트 값 모두 비교 ([0][0], [0][1], [0][2]...) 후 좌표에 맞는 값을 X로 표시
    stop = 0
    for i in range(5):
        for j in range(5):
            if my_list[i][j] == num: 
                my_list[i][j] = "X"
                stop = 1
                break   # break 입력하지 않아도 프로그램은 돌아감. 그 이후 비교를 안돌리기 위함.
                # break -> for j in range(5)만 빠져나와서 for i in range(5)로 돌아감
        if stop == 1: break