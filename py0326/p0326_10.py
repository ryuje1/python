# 가장 핵심 꼭 알아두기~~~~

# 숫자 2개를 입력 받아 사칙연산 결과 값을 출력하시오.
# format() 함수 사용
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2

a = int(input("1. 숫자를 입력해주세요."))
b = int(input("2. 숫자를 입력해주세요."))
print(a, b)
print1 = "{} + {} = {}".format(a, b, a+b)
print2 = "{} - {} = {}".format(a, b, a-b)
print3 = "{} * {} = {}".format(a, b, a*b)
print4 = "{} / {} = {:.0f}".format(a, b, a/b)
print(print1)
print("{} + {} = {}".format(a, b, a+b))
print(print2)
print(f"{a} - {b} = {a-b}")
print(print3)
print(print4)

# 국어, 영어, 수학 점수를 입력 받아 평균을 출력하시오.
# 합계 : 240
# 평균 : 80.00

kor = int(input("국어 점수를 입력해주세요."))
eng = int(input("영어 점수를 입력해주세요."))
mat = int(input("수학 점수를 입력해주세요."))
print("국어 점수 :", kor)
print("영어 점수 :", eng)
print("수학 점수 :", mat)

total = kor+eng+mat
avg = total/3

print("합계 :", total)
total_print = "합계 : {}".format(total)
print(total_print)

avg_print = "평균 : {:.2f}".format(avg)
avg_print_f = f"평균 : {avg:.2f}"
print(avg_print)
print(avg_print_f)