# 0327 정리~~~~~


# 변수에 대한 타입 설명
# 파이썬 타입
# bool 타입, 숫자 int 타입 / float 타입, str 타입


# bool 타입 - True, False (if문에서 필요)
if True: # 무조건 실행됨. if문은 결과 값이 참일때만 실행
    print("참입니다.")

if False: # 무조건 실행되지 않음
    print("거짓입니다.")
# if 문은 들여쓰기 중요. 들여쓰기 되어야 실행됨.

print(10>3) # True
if 10>3: # 결과 값이 True라서 실행됨
    print("정상")
else:
    print("비정상")
       
# int 정수형 - 소수점 X
print(1+2)
print(1+1.2)

# float 실수형 - 소수점 O
print("{:.2f}".format(10/3))     # fomat(), f함수 자주 사용하므로 알아두기 **중요

# str 문자열 -"" 또는 '' 안에 입력해야 함
print("안녕")
# print("안녕"+1) # 타입이 다른 경우 Error
print("안녕", 1)    # 타입이 다른 경우 출력하고 싶으면 쉼표(,) 사용
# 연산은 숫자일때만 가능, 문자열 타입은 그대로 붙음. => 안녕 1 출력됨


# 문자열 -> 숫자 타입 변경
print(int("1")+1)       # 문자열 1을 int 타입으로 변경 - 연산 가능. => 2 출력됨
# print(int("안녕1"))   # 숫자형태 문자열만 숫자 타입으로 변경 가능. => Error

# 숫자 타입 변경 - int / float 으로 변경 가능
print(int(1.5))     # 실수형 -> 정수형으로 타입 변경 - 소수점이 사라짐
# 문자열 float 타입을 int 타입으로 변경 안됨
# print(int("1.5")) # Error
print(float("1.5")) # 가능

print(str(1.5))     # 문자열 타입 변경

# ------------------------------------------------------------------------------------
# 변수
a = 10      # = 할당의 의미. a라는 변수에 10을 할당하라는 의미.
a = 5       # 다시 5를 할당하라는 의미. int 타입
b = 1.5     # float 타입
c = "안녕"  # str 타입

# print(c+a)  # str 타입 + int 타입 연산 불가. => Error
print(a+b)  # int 타입 + float 타입 연산 가능. => 6.5 출력됨


# List 타입 - 값을 여러 개 저장. 변수명 = [값1, 값2, 값3] 의 형식으로 선언. 변수명[0] 형식으로 값을 불러옴. **매우 중요
# 변수는 값 1개만 저장. List 배열은 공간을 새롭게 만들어 각 주소에 맞는 방에 값을 저장.
list_a = [1, 2, 3, 4]
print(list_a)   # 전체 출력
print(list_a[0])    # 첫번째 값 출력
print(list_a[0]+list_a[1]+list_a[2]+list_a[3])  # 전체 합계 출력


# input() : 데이터를 입력받는 명령어. 함수. !무조건 str 문자열 타입! => 타입 변경 필요
# score = input("데이터를 입력하세요.  ")
# print("입력 데이터 : ", score)

## 두 수를 입력 받아 합계, 평균을 출력하시오.
# num1 = int(input("1. 숫자를 입력하세요.  ")) # 타입 변경. => 변경하지 않으면 연산X. 그대로 붙여져서 출력됨.
# num2 = int(input("2. 숫자를 입력하세요.  "))
# print(f"입력받은 숫자 : {num1}, {num2}\t합계 : {num1+num2}\t평균 : {(num1+num2)/2:.2f}")

# if 조건문
# score = int(input("점수를 입력하세요.  "))
# if score >= 60: # 참이면 else문 실행하지 않고 빠져나옴
#     print("합격")
# else:
#     print("불합격")


# score = int(input("점수를 입력하세요.  "))

# if score >= 70:
#     print("합격")
# elif score >= 60: # 또다른 조건. elif는 여러 개 사용 가능.
#     print("재시험")
# else:
#     print("불합격")

## 90점 이상 A, B C D F ...
score = int(input("점수를 입력하세요.  "))

if score >= 90: print("A")      # 한 줄일때는 한 줄로 작성 가능
elif score >= 80: print("B")
elif score >= 70: print("C")
elif score >= 60: print("D")
else: print("F")