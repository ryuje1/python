# lotto 프로그램
# p0328_08.py, p0403_04.py 참고
import random

ran_list = random.sample(range(1,45+1), 6)   # 랜덤 번호 1-45 중 6개
my_list = []    # 내가 입력한 번호
lotto_list = [] # 당첨 번호 리스트
lotto_count = 0 # 당첨 개수

for i in range(6):
    # print("랜덤 번호 : ", ran_list)
    input_num = int(input(f"{i+1}번째 숫자를 입력하세요. (1-45)  "))
    if input_num not in my_list:    # 중복 확인
        my_list.append(input_num)

for j in range(6):
    if my_list[j] in ran_list:
        lotto_count += 1
        lotto_list.append(my_list[j])
        
print("랜덤 번호 6개 :", ran_list)
print("내가 입력한 번호 6개 :", my_list)
print(f"당첨 번호 : {lotto_list}, 당첨 개수 : {lotto_count}")