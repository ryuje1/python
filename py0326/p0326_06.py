# 변수 a 홍길동
# 변수 b 20
# 변수 c 22.5
# 변수 d True
# 변수 선언 후 값과 타입을 출력하시오.

a = "홍길동" # str
b = 20 # int
c = 22.5 # float
d = True # bool - True, False (대문자)

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

print(d)
print(type(d))

# 변수는 값을 입력할때 타입을 정의하고 변수에 다시 값을 넣으면 값이 변경됨 (타입 달라도 변경됨)
num = 100
print(num)

num = 200
print(num)

num = "안녕"
print(num)

# 변수 선언
num = 0
# 변수에 값을 더해서 자신의 변수에 입력
print(num)
num = num + 1
print(num)
num = num + 1
print(num)

num += 1    # num = num + 1
num -= 1    # num = num - 1
num *= 1    # num = num * 1
num /= 1    # num = num / 1
# 속도가 약간 더 빠름 이미지 처리할때 사용