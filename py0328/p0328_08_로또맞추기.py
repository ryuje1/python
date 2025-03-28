import random

## 랜덤 1-45번까지의 숫자 6개를 ran_list에 저장
## 입력받은 숫자 6개를 my_list에 저장
## 랜덤번호 : 
## 입력번호 : 
## 당첨개수 :
## 당첨번호 :

# ** 중요 외우기
my_list = []
lotto_count = 0     # 당첨개수
lotto_list = []     # 당첨번호
ran_list = random.sample(range(1,45+1),6)   # 랜덤번호 6개 리스트

i = 0
while i < 6:
    print("랜덤번호 : {}".format(ran_list))
    input_num = int(input("{}번째 숫자를 입력하세요. (1 - 45)  ".format(i+1)))
    if input_num not in my_list:
        my_list.append(input_num)
        i += 1

## 당첨 비교 프로그래밍 ran_list, my_lst

# for j in range(6):
#     for k in range(6):
#         if ran_list[j] == my_list[k]:
#             lotto_count += 1
#             lotto_list.append(my_list[k])
#             break

for j in range(6):
    if ran_list[j] in my_list:      # 파이썬만 가능. 
        lotto_count += 1
        lotto_list.append(my_list[j])
        
print("랜덤번호 : {}, 입력번호 : {}".format(ran_list, my_list))
print("당첨개수 : {}, 당첨번호 : {}".format(lotto_count,lotto_list))
# 2가지 방법 다 알아두기


## 랜덤 숫자를 반복해서 ran_list에 10개를 입력시키는 프로그램을 구현하시오.
## 단, 같은 숫자가 들어가지 않도록 하시오.
# ran_list = []
# i = 0

# while i < 6:
#     ran_input = random.randint(1, 45)
#     if ran_input not in ran_list:
#         ran_list.append(ran_input)
#         i += 1
# # => a_list = random.sample(range(1,45+1),6) 이렇게 한 줄로 실행할 수 있음 (파이썬만 가능)
# print(ran_list)