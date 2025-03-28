# 1. 두 숫자를 입력 받아, 합과 곱을 출력하시오.

# a = input("1. 숫자를 입력해주세요.")
# b = input("2. 숫자를 입력해주세요.")

# a = float(a)
# b = float(b)

# print(a+b)
# print(a*b)

# 2. a, b라는 변수에 입력 받아 a, b를 출력하고 a, b의 값을 교체해서 출력하시오.

# print(a, b)
# a, b = b, a
# print(a, b)

# print("두 수 출력 : ", a, b)
# c = a
# a = b
# b = c
# print("두 수 출력 : ", a, b)


# a = 100 # int 타입
# st = "안녕" # str 타입
# print("변수 값 : ", a)
# print("변수 값 : "+a) # 오류 발생 - 다른 타입일 때 +연산자 사용할 수 없음. 다른 타입은 쉼표(,) 사용
# print("변수 값 : ", st)
# print("변수 값 : "+st) # 같은 타입일 경우 +연산자 가능

a = 10
b = 5
print(a, "+", b, "=", a+b)

c = 100
d = 7
print(c, "*", d, "=", c*d)
print("%d * %d = %d" % (c, d, c*d))
print(c, "/", d, "=", c/d)
print("%d / %d = %07.2f" % (c, d, c/d)) # 나누기는 무조건 float