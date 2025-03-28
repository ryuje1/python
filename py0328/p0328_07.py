## 입력한 숫자를 5번 반복해서 리스트에 추가하는 프로그램 구현

# num_list = []
# for i in range (10):
#     num = int(input("숫자를 입력해주세요.  "))
#     # num이 num_list에 있는지 확인해서 있으면 제외, 없으면 입력
#     if num not in num_list: num_list.append(num)    # not in : 없는지 확인
# print(num_list)


num_list = []
i = 0   # i=1 로 설정할거면 while i <=10, .format(i) 로 하면 바꾸면 됨
while i < 10:
    num = int(input("{}번째 숫자를 입력해주세요.  ".format(i+1)))
    if num not in num_list: # 입력받은 숫자가 리스트에 없으면
        num_list.append(num)    # 리스트에 입력받은 숫자 추가
        i += 1  # 반복횟수 증가
        # 중복인 숫자는 i 증가하지않고 넘어감 -> 다시 처음부터 반복
print(num_list)



# input_list = [1, 5, 10, 9, 8, 20]

# a = 5
# if a in input_list: # input_list 안에 a가 포함이 되어있는지 확인
#     print("{}가 존재합니다.".format(a))
# else:
#     print("{}가 존재하지 않습니다.".format(a))


# i = 0
# while True:
#     print(i)
#     i += 1
# 무한대로 반복


# while문 : 조건에 해당이 되면 반복 - 무한 반복 가능
# i = 0
# while i < 10:
#     print(i)
#     i += 1  # 1씩 증가
# print("-"*50)

# for문 : 횟수만큼 반복 진행
# for j in range(10):
#     print(j)
    
# 위의 while문, for문은 같은 뜻. 실행하면 같은 값이 출력됨