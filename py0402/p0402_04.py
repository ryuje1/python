## 함수
# 함수를 사용하면 코드를 줄일 수 있음

## 두 수를 입력받아 사칙연산(+, =, *, /)을 출력하시오.
def cal(x, y):
    print("더하기 :", x + y)
    print("빼기 :", x - y)
    print("곱하기 :", x * y)
    print("나누기 :", x / y)
    return x + y    # x+y 값을 함수 호출 시점에 리턴해줌

num1 = int(input("1. 숫자를 입력해주세요.  "))
num2 = int(input("2. 숫자를 입력해주세요.  "))
result1 = cal(num1, num2)     # 함수 호출, 리턴 값을 result1 변수에 저장

num3 = int(input("3. 숫자를 입력해주세요.  "))
num4 = int(input("4. 숫자를 입력해주세요.  "))
result2 = cal(num3, num4)     # 함수 호출, 리턴 값을 result2 변수에 저장

num5 = int(input("5. 숫자를 입력해주세요.  "))
num6 = int(input("6. 숫자를 입력해주세요.  "))
result3 = cal(num5, num6)     # 함수 호출, 리턴 값을 result3 변수에 저장

# 결과 값 중 합계를 모두 더해서 총 합계를 구하시오.
print("총 합계 : {}".format(result1 + result2 + result3))

# def add(x, y):
#     print("x:", x)
#     print("y:", y)
#     print("x+y:", x + y)
    
# # 특정 값
# a = 10
# b = 20
# c = 30
# d = 40

# add(a, b)
# add(a, c)
# add(a, d)
# add(c, d)

# # 함수 선언 
# # def 함수명(매개변수) 형식. 
# # 매개변수 없으면 그냥 (), 매개변수가 없어도 리턴 값은 있을 수 있음
# # 변수명 => 명사, 함수명 => 동사를 많이 사용
# def add():
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")

# print("누군가 오고 있어요.")
# print("인사")
# add()   # 함수 호출

# print()     # 변수 뒤에 ()가 있으면 함수

# # 함수 선언
# def cal(x, y):  # def = define 정의하다
#     result = x + y
#     print(result)
#     result2 = x - y
#     print(result2)
#     result3 = x * y
#     print(result3)
#     result4 = x / y
#     print(result4)

# a, b = 10, 20
# cal(a, b) # 함수 호출

# c, d = 100, 200
# cal(c, d)

# e, f = 50, 100
# cal(e, f)