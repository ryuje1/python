## 구구단 출력
## 2 X 1 = 2

for i in range(2, 10):
    for j in range(1, 10):
        print("{} X {} = {}".format(i, j, i*j),end="  ")
    print()
# 구구단 가로로 출력

print("-"*50)

for i in range(1, 10):
    for j in range(2, 10):
        print("{} X {} = {}".format(j, i, i*j),end="  ")
    print()
# 구구단 세로로 출력 => i, j 위치 바꾸기

## 은행 가면 001 002 003 ... 010 011 012 ... 999 공백이 0으로 채워짐

# for i in range(1, 1000): # 000 부터 출력하고 싶으면 range(0, 1000)
#     print("{:03d}".format(i))   # 공백 0으로 채우고 3자리 출력