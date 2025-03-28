# 이름, 국어 성적, 영어 성적, 수학 성적을 입력 받아 합계와 평균을 출력하시오.
# 이름 : 홍길동
# 합계 : 300
# 평균 : 100.0 소수점은 1자리까지 출력하시오.

# a = input("이름을 입력해주세요.")
# b = int(input("국어 성적을 입력해주세요.")) # b = int(b)
# c = int(input("영어 성적을 입력해주세요.")) # c = int(c)
# d = int(input("수학 성적을 입력해주세요.")) # d = int(d)
# e = int(input("과학 성적을 입력해주세요.")) # e = int(d)
# print("이름 :", a)
# print("국어 :", b)
# print("영어 :", c)
# print("수학 :", d)
# print("과학 :", e)

# b = float(b)
# c = float(c)
# d = float(d)

# 합계, 평균 변수 **중요
# total = b+c+d+e
# avg = (b+c+d+e)/4

# print("합계 :", b+c+d+e)
# print("합계 : %d" % total)
# print("평균 : %0.1f" % avg) # 중요

# 값 입력받고 문자열 타입을 int 또는 float 타입으로 변경 후 합계, 평균 계산
# input 입력받은 값 = 문자열 타입 **중요


# print -> \n 엔터키, \t tab키
# print("안녕하세요.\n반갑습니다.\t저는 홍길동이라고 합니다.")

# format(), f함수 **중요
# format() 문자형태 지정 함수
a = 10
b = 3
print("%d / %d = %.2f" % (a, b, a/b))
print("{} / {} = {:f}".format(a, b, a/b))

str_print = "{} / {} = {:7.2f}".format(a,b,a/b) # format 에서는 %f가 아닌 :f 사용, 앞은 위치 뒤는 값
print(str_print)

# f함수 = format()
str_print2 = f"{a} / {b} = {(a/b):.2f}" # f함수에서는 변수 뒤에 :f 사용, 위치와 값이 동시에 옴
print(str_print2)