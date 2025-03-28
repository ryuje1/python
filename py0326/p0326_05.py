# 변수
# 재사용하기 위함
# 타입은 총 4가지

# aaa = 1
# bb = True
# b = "안녕"

# 변수명 = 데이터 값
# 수학에서의 = 같다를 의미, 프로그래밍에서의 = 할당한다는 의미

# 변수명 규칙
# 대소문자 구분함
# 특수문자는 언더바(_)만 가능 ($a, &&bab 불가능 / _abc, _num, n_1 가능)
# 숫자가 제일 앞에 올 수 없음 (100top, 7up 불가능)
# 숫자가 중간에 오는 것은 가능 (top100, up7, a1 가능)
# 예약어 사용 불가 (True, False, None, and, or, for ...)
D = 100
d = 100
true = 100 # True 예약어, true 는 가능하지만 오해의 소지가 있어 잘 쓰지 않음

a = 11 # 11 = a 는 불가능
b = 6
# print
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# bool타입 : True, False
aaa = True
bbb = False

print(aaa)
print(type(aaa))

# int타입 : 정수 (소수점 X)
ccc = 100
print(ccc)
print(type(ccc))

# float타입 : 실수 (소수점 O)
ddd = 3.14
print(ddd)
print(type(ddd))

# str타입 : 문자열
eee = "안녕"
print(eee)
print(type(eee))