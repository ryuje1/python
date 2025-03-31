# 5X5 리스트 - 0으로 초기화 (1)
sample_list = [[0]*5 for i in range(5)]
print(sample_list)

# # 5X5 리스트 - 0으로 초기화 (2)
# sample_list = list() # list 초기화. 초기화 : 값을 처음으로 0 또는 공백으로
# for i in range(5):
#     temp = []
#     for j in range(5):
#         temp.append(0)  # [0, 0, 0, 0, 0] / j 값을 주면 [0, 1, 2, 3, 4]
#     sample_list.append(temp) # [[0, 0, 0, 0, 0]]
# => 6줄이 sample_list = [[0]*5 for i in range(5)] 1줄과 동일
# print(sample_list)

# a_list = [i+1 for i in range(25)] # 1, 2, 3, 4, 5... 25
# a_list = [[1, 2, 3, 4, 5],
#           [6, 7, 8, 9, 10],
#           [11, 12, 13, 14, 15],
#           [16, 17, 18, 19, 20],
#           [21, 22, 23, 24, 25]]

# import random
# # 1. 순차적 리스트 생성
# sample_list = [i+1 for i in range(25)]
# # 2. 리스트 섞기
# random.shuffle(sample_list)  # 리스트의 숫자가 랜덤으로 섞임
# # 3. 2차원 초기화 리스트 생성
# a_list = [[0]*5 for i in range(5)]  # 깊은 복사
# # 4. 2차원 리스트에 랜덤 리스트의 값을 입력
# for i in range(5):
#     for j in range(5):
#         a_list[i][j] = sample_list[5*i+j]   # 랜덤 숫자가 들어감
# # 5. 5X5 출력
# for i in range(5):
#     for j in range(5):
#         print(a_list[i][j], end="\t")
#     print()


# # 5X5 리스트 초기화 **중요
# # a_list = [[0]*5]*5 # 얕은 복사.
# a_list = [[0]*5 for i in range(5)]  # [0][0][0][0][0]를 5개 만듦. 깊은 복사. 이렇게 만들어야 함
# print(a_list)

# for i in range(5):
#     for j in range(5):
#         a_list[i][j] = 5*i+(j+1)  # 1, 2, 3.... 25
# print(a_list)



# # 1-25
# import random
# a_list = [i+1 for i in range(25)] # 1-25
# print(a_list) # 1, 2, 3, 4... 25
# random.shuffle(a_list)
# print(a_list) # 랜덤으로 섞여진 리스트 출력

# # 2차원 배열 출력
# # 1 2 3 4 5
# # 6 7 8 9 10
# # 11 12 13 14 15
# # 16 17 18 19 20
# # 21 22 23 24 25

# a_list = [[1, 2, 3, 4, 5],
#           [6, 7, 8, 9, 10],
#           [11, 12, 13, 14, 15],
#           [16, 17, 18, 19, 20],
#           [21, 22, 23, 24, 25]]

# for i in range(5):
#     for j in range(5):
#         print("{:02d} ".format(a_list[i][j]), end="")
#     print()


# # 2차원 배열 출력
# # 1 2 3
# # 4 5 6
# # 7 8 9
# a_list = [[1, 2, 3],    # [0][0], [0][1], [0][2]
#           [4, 5, 6],    # [1][0], [1][1], [1][2]
#           [7, 8, 9]]    # [2][0], [2][1], [2][2]

# for i in range(3):  # 0, 1, 2
#     for j in range(3):  # 0, 1, 2
#         print("{} ".format(a_list[i][j]), end="")
#     print()


# # 1차원 리스트
# aa = [10, 20, 30]
# print(aa[0]) # 10 출력

# # 2차원 리스트  **중요
# aa = [[1, 2, 3, 4],     # [0]
# #    [0][0], [0][1], [0][2], [0][3] 
#       [5, 6, 7, 8],     # [1]
#       [9, 10, 11, 12]]  # [2]
# print(aa[0]) # [1, 2, 3, 4] 출력
# print(aa[0][0]) # 1 출력


# ## 리스트 값 변경
# a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a_list[5] = 10  # 5번 자리 값을 10으로 변경하라는 의미
# print(a_list) # [1, 2, 3, 4, 5, 10, 7, 8, 9, 10] 출력

# # 값을 변경할 때 1:2는 2의 위치 값이 포함. 다른 경우에는 2의 앞의 값
# a_list[1:2] = [100, 200]
# print(a_list) # [1, 100, 200, 3, 4, 5, 10, 7, 8, 9, 10] 출력

# # 역순 출력
# a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a_list[::-1]) # 전체 다 출력하는데 역순으로 출력하라는 의미. [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 출력

# a_list = [1, 2, 3, 4, 5]
# # print(a_list[5]) # 범위를 벗어났기 때문에 Error

# # 모양 출력
# for i in range(10):
#     for j in range(i): # 0, 1, 2, 3...9
#         print("*", end="")
#     print()

# for i in range(10):
#     if i% 2 == 0: continue
#     print(i)

# continue, break, pass **자주 사용
# continue - 그 위치에서 중지 후 다시 for문 실행. 다시 위로 가서 실행
# ex) 1 - 10 까지 진행할 때 1,2,3-continue-,4,5,6,7,8,9,10 => 3번만 실행X 4-10번까지는 진행. 총 9번 진행

# break - 반복문 빠져나옴
# ex) 1 - 10 까지 진행할 때 1,2,3-break- 반복문 끝

# pass - 실행할 구문이 없음. 공백으로 쓰면 오류나니까 pass 작성. for문을 계속 반복. 밑의 꺼는 실행
# ex) 1 - 10 까지 진행할 때 1,2,3-pass-,4,5,6,7,8,9,10 => 총 10번 진행

## 입력한 숫자의 합이 50을 넘으면 프로그램을 종료하고 총합을 구하시오. **헷갈린 부분
## 입력 숫자 중 5의 배수는 제외시킬 것

# sum = 0

# while True:   # 정해진 범위가 없으므로 무한반복
#     if sum < 50:
#         num = int(input("숫자를 입력해주세요.  "))
#         if num % 5 == 0: 
#             print("5의 배수는 제외")
#             continue # 실행을 1번 중지
#         sum += num
#         print("합계 : {}".format(sum))
#     else:
#         print("-프로그램 종료-") 
#         break



# ## 1-100 까지의 숫자의 합을 구할 때 합계가 200을 넘을 때 숫자를 출력하시오.
# ## 1+2+3+4.... 합계가 200이 넘는 위치 값을 출력하시오.
# ## break : 반복문 중지

# i = 0 # 파이썬에서는 초기화할 필요 X. 자바에서는 필요함
# sum = 0
# for i in range(100):
#     sum += i
#     if sum >= 200:
#         break
# print("i : {}, sum : {}".format(i, sum))
# print("i 이전 : {}, sum : {}".format(i-1, sum-i)) # 200 이전 값 출력


# ## 반복문 - for, while
# a_list = [i+1 for i in range(100)] # 1-100까지의 리스트 생성
# print(a_list)

# ## a_list 홀수의 합계를 구하시오.
# ## a_list[] % 2 == 0
# sum = 0
# for i in a_list:
#     if i % 2 == 1:
#         sum += i
# print(f"홀수 합계 : {sum}")

# for j in a_list:
#     if j % 2 == 0:
#         sum += j
# print("짝수 합계 : {}".format(sum))


# import random
# # random.random() 함수 : 0 <= x < 1 사이의 랜덤 실수를 가져옴.
# print(random.random())
# print(int(random.random()*10)+1) # 1-10 사이 정수 1개. randint 쓰는 것과 동일 (java 에서는 이렇게 사용해야 함)
# print(int(random.random()*10)+0) # 0-9 사이 정수 1개. randint 쓰는 것과 동일
# print(random.randint(1, 10)) # 1-10 사이 정수 1개. 파이썬에만 있음

# import random
# a_list = [i+1 for i in range(45)]   # 1부터 45까지 순서대로
# print(a_list)

# random.shuffle(a_list) # 순서 무작위
# print(a_list[:6])
# # ran_list = random.sample(range(1, 45), 6) 와 동일하게 랜덤 6개 뽑음



# ## 로또 프로그램  **중요
# # 6개 랜덤 숫자와 입력 숫자 6개 출력하시오.
# import random

# lotto = []  # [i+1 for i in range(45)] 하고 ran_list range(1,45) 위치에 lotto 넣어도 가능
# my_input = []
# ran_list = random.sample(range(1, 45), 6)   # 1-45 사이 숫자 중 6개를 중복없이 가져옴. 파이썬에만 있음
# # 파이썬이 아닌 경우 아래처럼 작성
# # for i in range(6):
# #     lotto.append(random.randint(1,45)) # 중복 가능

# for i in range(6):
#     num = int(input("{}. 숫자를 입력해주세요.  ".format(i+1)))
#     my_input.append(num)
#     if num in ran_list:
#         lotto.append(num)
# print("랜덤 숫자 : {}, 입력 숫자 : {}".format(ran_list, my_input))
# print("당첨번호 : {}".format(lotto))



# ## 10번의 숫자를 입력 받아 합계를 구하시오. for문, while문 사용
# # for문
# sum = 0
# for i in range(10):
#     num = int(input("{}. 숫자를 입력해주세요.  ".format(i+1)))
#     sum += num
# print("합계 : {}".format(sum))

# # while문 * 주의 : 변수는 while문 밖에 선언해주고 i값 증가해줘야 함
# i = 0
# sum = 0
# while i < 10:
#     num = int(input("{}. 숫자를 입력해주세요.".format(i+1)))
#     sum += num  # sum = sum + num 과 동일
#     i += 1
# print(f"합계 : {sum}")


# ## while문  **중요
# i = 0 # 반복에 대한 변수 값을 반드시 주어야 반복문 조건 실행.
# while i < 10:           # 0-9까지 10번 반복
#     print(i)
#     i = i+1


# ## for문    **중요
# for i in range(10):     # 0-9까지 10번 반복
#     print(i)