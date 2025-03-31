a = 10
a_list = [1, 2, 3, 4, 5]

print("a : ", a)
print("a_list : ", a_list)

a_list[0] = 100
print("a_list : ", a_list) # [100, 2, 3, 4, 5]

# a변수와 b변수는 다른 변수.
b = a
b = 1000
print("a : ", a) # 10
print("b : ", b) # 1000

# **매우 중요
# 새롭게 복사 : 깊은 복사. 다른 곳을 바라봄
a_list = [1, 2, 3, 4, 5]
b_list = [*a_list]
b_list[1]= 200
print(a_list) # [1, 2, 3, 4, 5]
print(b_list) # [1, 200, 3, 4, 5]

# ## 주소값 복사 : 얕은 복사 - 깊은 복사보다 훨씬 많이 사용
# # a_list, b_list 다른 리스트인가?? => 다르지 않음. 위치 값을 저장하기 때문에 같은 곳을 바라봄.
# # 값이 하나인 변수에서 가능한 방법
# a_list = [1, 2, 3, 4, 5]
# b_list = a_list
# b_list[1]= 200
# print(a_list) # [100, 2, 3, 4, 5] 여야 하는데 [100, 200, 3, 4, 5] 출력됨


# a_list = [1, 2, 3, 4, 5]
# sum = 0
# for i in a_list:    # range(범위) 말고도 list 사용 가능 => a_list 요소들을 1개씩 사용 가능
#     sum += i
# print("합계 : {}".format(sum))


# ## 구구단   **중요

# ## 2 X 1 = 2    2 X 2 = 4 ...
# ## 3 X 1 = 2    3 X 2 = 6 ...
# for i in range(2, 9+1):
#     print("[ {}단 ]".format(i))
#     for j in range(1, 9+1):
#         print("{} X {} = {}".format(i, j, i*j), end="   ")
#     print()
    
# print()

# ## 2 X 1 = 2    3 X 1 = 3 ...
# ## 2 X 2 = 4    3 X 2 = 6 ...
# for i in range(1, 10):
#     for j in range(2, 10):
#         print("{} X {} = {}".format(j, i, i*j), end="   ")
#     print()