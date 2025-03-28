# 0326 복습

# 파이썬 변수타입
# 1. bool 타입 - True, False
# 2. 숫자 int 타입 - 정수, float 타입 - 실수
# 3. str 타입 - 문자열

# print()
print("안녕")

# 변수 선언
# 변수명 = 데이터 값
# = 는 값을 할당하라는 의미
# abc = 10
# 변수 = 20
# num = 30
# 한글 써도 되나 되도록이면 영어 사용하기

# print()
# print("안녕")
# print("안녕", abc)
# print("입력된 숫자 : %d" % (abc))
# print("입력된 숫자 : {}".format(abc)) # format() **중요
# print(f"입력된 숫자 : {abc}") # f함수 **중요


# 입력 - input
# input으로 입력받은 값은 무조건 문자열 str타입이기 때문에 타입 변환을 해줘야 함. int() 또는 float()
# input 만으로는 의미가 없어서 변수에 값을 넣음
# num1 = int(input("숫자를 입력하세요. ")) # str 타입 => int 타입으로 변환
# num2 = int(input("숫자를 입력하세요. "))
# print("입력된 숫자 : {}, {} / 합계 : {}".format(num1, num2, num1+num2))
# print(f"입력된 숫자 : {num1}, {num2} / 합계 : {num1+num2}")


# 학생 성적 프로그램
# 이름, 국어 성적, 영어 성적, 수학 성적을 입력받아 합계와 평균을 출력하는 프로그램을 구현하시오.
print("-"*50)
print("학생 성적 프로그램")
print("-"*50)

name = input("이름을 입력해주세요. ")
kor = int(input("국어 성적을 입력해주세요. "))
eng = int(input("영어 성적을 입력해주세요. "))
mat = int(input("수학 성적을 입력해주세요. "))
total = kor+eng+mat 
avg = (kor+eng+mat)/3
print()
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name, kor, eng, mat, total, avg))
# print("{}\t{}\t{}\t{}\t{}\t{:.1f}".format(name, kor, eng, mat, kor+eng+mat, (kor+eng+mat)/3)) 도 가능