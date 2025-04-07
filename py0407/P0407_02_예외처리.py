# 예외처리
# 프로그램 하다보면 Error로 프로그램이 종료될 때가 있는데 이를 방지

# 1. 구문 Error
# 2. 런타임 Error

# print("데이터 출력")
# # priint("데이터 출력")   # 구문 Error - 오타

# a_list = [1, 2, 3, 4, 5]
# for a in a_list:
#     print(a)

# for i in range(6):
#     print(a_list[i])     # 구문에 Error는 없지만 실행 시 Error - 런타임 Error
# # -> 프로그램이 종료됨

# 숫자만 입력 가능 그 외에는 Error 발생 #
# print("1. 학생 성적 출력")
# choice = int(input("원하는 번호를 입력하세요.  "))
# print("입력한 번호 :", choice)


# Error를 처리하는 방법
# - if 조건문을 사용해서 처리
# - 예외처리 사용

# if문 사용해서 처리 #
# print("1. 학생 성적 출력")
# choice = input("원하는 번호를 입력하세요.  ")
# if choice.isdigit():    # 숫자로 변환 가능한지 확인
#     choice = int(choice)
# else: 
#     print("숫자만 입력이 가능합니다.")
# print("입력한 번호 :", choice)

# 예외처리 사용 #
# 강제로 프로그램 종료되는 문제 해결, Error에 대한 문제점 확인 가능
print("1. 학생 성적 출력")
choice = input("원하는 번호를 입력하세요.  ")
try:            # 예외처리
    choice = int(choice)
except Exception as e: 
    print("숫자만 입력이 가능합니다.")
    print(e)    # Error 구문 출력 가능
print("입력한 번호 :", choice)