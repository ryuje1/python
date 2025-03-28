## 3, 5, 7, 9 홀수단만 출력

# for i in range(2, 9+1):     # range(3, 9+1, 2) 도 가능
#     if i%2 == 1:            # == 0 이면 짝수단
#         print("[{}단]".format(i))
#         for j in range(1, 9+1):
#             print("{} X {} = {}".format(i, j, i*j), end="")
#         print()
        
##시작단과 끝나는 단을 입력받아 출력하시오
# 2, 6 -> 2단~ 6단 까지 출력

num1 = int(input("1. 숫자를 입력하세요.  "))
num2 = int(input("2. 숫자를 입력하세요.  "))

# if num1 > num2:
#     num1, num2 = num2, num1

if num1 > num2:
    t = num1
    num1 = num2
    num2 = t

for i in range(num1, num2+1):
    print("[{}단]".format(i))
    for j in range(1, 9+1):
        print("{} X {} = {}".format(i, j, i*j))
    print()
    
## 구구단 출력
# 2중 for문
# for i in range(2, 9+1):
#     print("[{}단]".format(i))
#     for j in range(1, 9+1):
#         print("{} X {} = {}".format(i, j, i*j), end="")     # 옆으로 출력
#     print()     # 단마다 줄바꿈



## 두 수를 입력받아, 두 수 사이의 합계를 구하시오.

# num1 = int(input("1. 숫자를 입력하세요.  "))
# num2 = int(input("2. 숫자를 입력하세요.  "))
# print(num1, num2)

# sum = 0
# i = 0
# t = 0

# if num1 > num2: # if문 비교 num1, num2 num2가 더 큰지 확인
#         t = num1
#         num1 = num2
#         num2 = t  
        # num1, num2 = num2, num1 과 같은 말 (파이썬에서만 가능해서 위의 형태도 알아야 함)

# for i in range (num1, num2+1):  # num2까지 하려면 num2+1 해야 함  
#     sum = sum + i
    # print("i : {}, sum : {}".format(i, sum))
# print("{}에서 {}까지의 합계 : {}".format(num1, num2, sum))