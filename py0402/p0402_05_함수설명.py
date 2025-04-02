def cal(*a, b=10):      # (가변매개변수, 키워드 매개변수) 함께 사용할 경우, 매개변수 키워드
    result = b
    for i in a:
        result += i
    return result

print(cal(1, 2, 3, 4, 5, b=100))    # b=100 하지 않으면 전부 가변매개변수로 인식


# # 키워드 매개변수 : 들어오지 않으면 디폴트값 설정
# def cal(a, b=10):       # 키워드 변수는 무조건 마지막에 있어야함 (a=10, b)는 Error
#     return a+b
# print(cal(1))


# # print() 함수는 매개변수가 가변매개변수
# print(1, 2, 3, 4, 5)
# print(1, 2)


# # 가변매개변수 사용
# def cal (*num):     # * : 전개 연산자 1, 2, 3, 4, 5... 각각 분리
#     result = 0
#     for n in num:
#         result += n
#     return result

# print("2개 합계 :", cal(1, 2))
# print("3개 합계 :", cal(10, 20, 30))
# print("4개 합계 :", cal(1, 2, 3, 4))


# def cal(n1, n2):
#     return n1 + n2

# def cal2(n1, n2, n3):
#     return n1 + n2 + n3

# n1 = 10
# n2 = 20
# n3 = 30
# result = cal(n1, n2)
# print(result)

# result2 = cal2(n1, n2, n3)
# print(result2)

# # global 변수 : 전역 변수를 가져옴
# def func1():
#     global a    # 전역 변수 호출
#     a = 20
#     # a = 20      # 지역 변수 => 함수 벗어나면 사라짐.

# a = 10
# print("a :", a)     # 10
# func1()
# print("a :", a)     # 10 / global 선언 시 20


# # 매개변수로 그룹 변수 전달하는 형태 - 주소 값이 넘어가서 같은 곳을 바라봄. return 받을 필요 없이 바로 값이 변경됨.
# # 국어 점수 변경 함수 선언
# def cal(ss):
#     ss['kor'] = int(input("수정할 국어 점수를 입력하세요.  "))
#     ss['total'] = ss['kor'] + ss['eng'] + ss['math']
#     ss['avg'] = ss['total'] / 3
    
# print("[ 학생 성적 수정 ]")
# s = {"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100.0, "rank":1}
# # 국어 점수 변경 함수 호출
# cal(s)      # 변경된 국어 점수 반영
# print("수정된 국어 점수 :", s['kor'])


# # 매개변수로 일반 변수 전달하는 형태 - return으로 값을 돌려줘서 입력을 시켜야 함
# # 국어 점수 변경 함수 선언
# def cal(kor):
#     kor = int(input("수정할 국어 점수를 입력하세요.  "))
#     return kor  # 일반변수 = 함수 내에서 변경한 값은 return으로 넘겨줘야 변경 가능
    
# print("[ 학생 성적 수정 ]")
# kor = 100
# eng = 100
# math = 100
# # 국어 점수 변경 함수 호출
# kor = cal(kor)      # 변경된 국어 점수 반영
# print("수정된 국어 점수 :", kor)



# def cal(b_list):
#     b_list[0] = 100     # 그룹으로 되어있는 변수는 주소값이 가서 함수 벗어나도 사라지지 않음. - list, dict, tuple
#     b_list[1] = 200

# a_list = [0, 0]   # 리스트 타입 변수 - 주소값 O
# a_list[0] = 10
# a_list[1] = 20
# print("함수 호출 전 a_list :", a_list[0], a_list[1])

# cal(a_list) # 함수 호출     b_list = a_list 주소값 복사
# print("함수 호출 후 a_list :", a_list[0], a_list[1])    # 100, 200 출력



# # 함수 선언
# def cal(a, b):
#     a = 100     # 지역 변수 - 함수 내에 선언되어있는 일반 변수. 함수를 벗어나면 사라짐. - bool, int, float, str
#     b = 200

# # -------------------
# # 함수 바깥
# a = 10          # 전역 변수
# b = 20
# print("함수 호출 전 a, b :", a, b)

# # 함수 호출
# cal(a, b)
# print("함수 호출 후 a, b :", a, b)    # 10, 20 출력



# ## 이름, 국어, 영어, 수학 점수를 입력받아 합계, 평균을 출력하시오.
# students = [{"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100.0, "rank":1},
#             {"no":2, "name":"유관순", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2},
#             {"no":3, "name":"이순신", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2}]

# def stu_print(): 
#     for s in students:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    
# print("1. 학생 성적 입력")
# print("2. 학생 성적 출력")
# choice = int(input("원하는 번호를 입력하세요.  "))
# if choice == 2:
#     stu_print()     # 함수 호출



## 이름, 국어, 영어, 수학 점수를 입력받아 합계, 평균을 출력하시오.

# # 함수 선언
# def cal(kor, eng, math):
#     # total = kor + eng + math
#     # avg = total / 3
#     # return total, avg
#     return kor+eng+math, (kor+eng+math)/3

# no = 1
# name = input("이름을 입력해주세요.  ")
# kor = int(input("국어 점수를 입력해주세요.  "))
# eng = int(input("영어 점수를 입력해주세요.  "))
# math = int(input("수학 점수를 입력해주세요.  "))
# total, avg = cal(kor, eng, math)
# print("합계 :", total, "평균: ", avg)



# ## 직사각형 넓이와 둘레를 구하는 프로그램을 구현하시오.
# ## 넓이 : 가로 * 세로, 둘레 : 가로길이*2 + 세로길이*2

# ## 가로, 세로 길이를 입력받아 넓이와 둘레를 구하시오.
# ## 함수를 사용할 것
# ## 파이썬은 리턴값 2개할 수 있음. 변수도 2개

# def cal(num1, num2):
#     result1 = num1 * num2
#     result2 = num1*2 + num2*2
#     return result1, result2

# num1 = int(input("가로 길이를 입력해주세요.  "))
# num2 = int(input("세로 길이를 입력해주세요.  "))
# result1, result2 = cal(num1, num2)
# # print("직사각형의 넓이 : {}, 둘레 : {}".format(result1, result2))
# print("넓이 :", result1, "길이 :", result2)



# ## 입력을 5개를 받아 짝수만 모두 더한 값을 출력하시오.

# # cal 함수 선언
# def cal (n_list):
#     sum = 0
#     for n in n_list:
#         if n % 2 == 0: sum += n
#     return sum

# n_list = [0]*5
# for n in range(5):
#     n_list[n] = int(input("숫자 입력  "))
# result = cal(n_list)
# print("짝수의 합 :", result)



## 함수를 사용해서 두 수를 입력 받아
## 10 - 20 입력 받으면 10+11+12+13...20 출력하시오.

# def add(n1, n2):
#     sum = 0
#     for i in range(n1, n2+1):
#         sum += i
#     print("합계 :", sum)
        
    
# n1 = int(input("1. 숫자를 입력하세요.  "))
# n2 = int(input("2. 숫자를 입력하세요.  "))
# add(n1, n2)

# # 큰 수를 먼저 넣어도 바꿔서 계산되도록
# def add(n1, n2):
#     sum = 0
#     # if n1 > n2: n1, n2 = n2, n1
#     t = 0
#     if n1 > n2:
#         t = n1
#         n1 = n2
#         n2 = t
#     for i in range(n1, n2+1):
#         sum += i
#     print("합계 :", sum)
    
# n1 = int(input("1. 숫자를 입력하세요.  "))
# n2 = int(input("2. 숫자를 입력하세요.  "))
# add(n1, n2)
        


# 함수 사용
# 1. 중복 코드가 있을 때
# 2. 소스가 너무 복잡할 때
# 먼저 프로그램을 모두 구현하고 중복되고 있는지 확인 후 함수 사용 (처음부터 함수 사용 X)

# ## num1, num2, num3 값을 입력받아 합계와 평균을 구하시오.
# # 함수 선언
# def add(kor, eng, math):
#     return kor + eng + math

# kor = int(input("국어 점수를 입력하세요.  "))
# eng = int(input("영어 점수를 입력하세요.  "))
# math = int(input("수학 점수를 입력하세요.  "))
# total = add(kor, eng, math)     # 함수 호출
# avg = total / 3

# print(kor, eng, math, total, avg)