# a, b = 100, 200 # 1번째 방법
# c = 300; d = 400 # 2번째 방법
# e = 500
# f = 600 # 3번째 방법

# # 관계 연산자 - True, False
# print(a==b)
# print(a!=b)
# print(a>b, a<b, a>=b, a<=b)

# 연산자 우선순위 : 산술(사칙연산) - 관계(<><=>=) - 논리(and or) 순서대로
# tab 들여쓰기 / shift+tab 들여쓰기 취소
# Home 키 - 문장 처음으로 이동 / End 키 - 문장 마지막으로 이동

# 조건식
# a = int(input("숫자를 입력하세요. "))
# if a < 100: # 조건이 참이면 실행 (True). !들여쓰기한 구문만 인식함!
#     print("입력한 값은 100보다 작은 수 입니다.")
# else: # 조건이 거짓이면 실행 False
#     print("입력한 값은 100보다 큰 수 입니다.")


# 양수, 음수 인지 확인 (0은 양수로)
# input_num = int(input("숫자를 입력하세요. "))
# if input_num >= 0:
#     print("양수입니다.")
# else:
#     print("음수입니다.")
    
# num -> 짝수인지 홀수인지 구현. num % 2 == 0
num = int(input("숫자를 입력해주세요. "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
    
# 3의 배수인지 아닌지
num = int(input("숫자를 입력해주세요. "))
if num % 3 == 0:
    print("3의 배수입니다.")
else: # if num % 3 != 0 과 같지만 if문을 많이 쓰면 속도가 느려져서 if~else 또는 if문 한번만 사용하는 것을 권장.
    print("3의 배수가 아닙니다.")