print(1)
print(2)
raise NotImplementedError   # 강제로 예외를 발생시킴 => 프로그램 구현이 아직 진행이 안되었다는 의미
print(3)


# try:        # 프로그램 구현 부분
#     print(1)
#     print(2)
#     # raise NotImplementedError   # 예외를 강제로 발생시킴
#     raise ZeroDivisionError
#     # choice = int(input("숫자를 입력하세요.  "))     # 문자 입력 시 1, 2, 5, 7 출력  / 숫자 입력 시 1, 2, 3, 4, 6, 7 출력
#     print(3)
#     print(4)
# except Exception as e:     # Error 났을 때 실행
#     print(e)
#     print(5)
# else:       # Error 나지 않았을때 실행
#     print(6)
# finally:    # Error 또는 Error 나지 않았을때 모두 실행
#     print(7)




# try:
#     num = int(input("원의 반지름을 입력하세요.  "))
#     print("원의 넓이 :", 3.14 * num**2)
# except Exception as e: print(e)
# else:    # try 구문에 Error가 없을 시 실행
#     pass



# a_list = ["52", "273", "32", "파이썬", "103"]

# list_number = []
# 숫자로 변환되는 것만 list_number에 저장하시오.

# if문 사용
# for a in a_list:
#     if a.isdigit():
#         list_number.append(int(a))
#     else: print("숫자 아님 :", a)
# print("숫자로 변환 :", list_number)

# 예외처리
# for a in a_list:
#     try:
#         list_number.append(int(a))
#     except Exception as e: print(e)     # Error 구문 출력
# print(list_number)