# a = 100
# b = 50

# b = 100, a = 50 값을 교체
# 이렇게 하려면 어떻게 값을 변경하면 될까요?
# b = 100
# a = 50

# print(a) # 100
# print(b) # 50

# 두 변수의 값을 교체하려면 추가적인 변수 c를 하나 두고 값을 보관하여 교체
# c = a
# a = b
# b = c

# a, b = b, a # 파이썬 a, b의 변수값 교체방법. 파이썬만 가능

# a = b
# b = a

# print(a) # 50
# print(b) # 50


# 입력 : input
# 출력 : print

# print(input("숫자를 입력하세요."))

# 변수() = 함수라고 부름. 함수란 어떠한 기능 구현을 말함.
# print()

# 입력 - 무조건 문자열 (str) 타입
# 타입 변경 - 정수 : int(), 실수 : float(), 문자열 : str() **중요
a = input("1. 숫자를 입력하세요.")
b = input("2. 숫자를 입력하세요.")
a = float(a) # str -> int, float
b = float(b) # str -> int, float
print(a)
print(b)
print(a,b)
print(type(a)) # str 문자열
print(type(b))
print(a+b) # 타입 변경하지 않으면 100+500 600이 나오지 않고 문자 뒤에 문자가 붙어 105가 됨