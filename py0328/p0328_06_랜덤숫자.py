## 숫자 맞추기 프로그램
import random

input_list = [] # 입력한 숫자 저장 리스트 타입
lotto = random.randint(1, 45) # 1-45 사이의 숫자 1개를 랜덤으로 가져옴
i = 0

for i in range (1, 10+1):
    print("{}번째 도전".format(i))
    input_num = int(input("1-45번 사이의 숫자를 입력하세요.  "))
    input_list.append(input_num) # input_list 리스트타입에 input_num 숫자 추가
    if lotto == input_num:
        print("당첨")
        break   # for문 종료
    elif lotto > input_num:
        print("틀렸습니다. {}보다 더 큰 수를 입력하세요~".format(input_num))
    else:
        print("틀렸습니다. {}보다 더 작은 수를 입력하세요~".format(input_num))

print("랜덤 번호 : {}".format(lotto))
print("입력 번호 : {}".format(input_list))