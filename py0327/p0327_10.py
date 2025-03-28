# 1-100까지 랜덤 숫자를 생성해서 정답을 맞추는 프로그램 구현하시오.
# 출력
# 도전 횟수 : 5
# 도전 번호 : [1, 2, 3, 4, 5]
# 랜덤 번호 : 5
import random
ran_num = random.randint (1, 100)   # 랜덤 숫자 생성
num = []    # num list 생성
n = 0   # n 변수 생성

for n in range (1, 11):     # 10번 반복
    in_num = int(input("숫자를 입력하세요.  "))
    num.append(in_num)      # 입력 숫자를 num 리스트에 저장
    if in_num == ran_num:
        print("정답 입니다. 입력 숫자 : {}".format(in_num))
        break
    elif in_num < ran_num:
        print("더 큰 숫자를 입력하세요. 입력 숫자 : {}".format(in_num))
    else:
        print("더 작은 숫자를 입력하세요. 입력 숫자 : {}".format(in_num))

print("도전 횟수 : {}".format(n))
print("도전 번호 : {}".format(num))
print("랜덤 번호 : {}".format(ran_num))