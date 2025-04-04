students = [{"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100.0, "rank":1},
            {"no":2, "name":"유관순", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2},
            {"no":3, "name":"이순신", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":2}]

# sorted() - 기존 리스트는 유지, 새로운 리스트 생성
# s_list와 students는 아예 다름
s_list = sorted(students, key=lambda x:x['name'])
print(s_list)
print("-"*60)
print(students)


# sort() - 기존의 리스트의 값을 변경시킴
# 합계 정렬 방법
# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['total'])
# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['total'], reverse=True)
# print(students)

# students.sort(key=lambda x:x['name'])   # 이름 순차정렬
# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['name'], reverse=True)  # 이름 역순정렬
# print(students)


# dict 타입은 sort() 함수 사용 불가
# students.sort()
# print(students) # 딕셔너리는 크기 비교 불가 => Error


# 람다식 lamda -> 함수 축약형
# lambda 매개변수:return값
# lambda a:a*20

# map(함수, 리스트) : 리스트에 함수를 적용해서 다시 리스트로 반환
# filter (함수, 리스트) : 리스트에 함수를 적용해서 조건에 맞는 (True인) 것만 다시 리스트로 반환

# filter 함수 관련
# a_list = [1, 2, 3, 4, 5]
# aa_list = []
# for i in a_list:
#     if i%2 == 0:
#         aa_list.append(i)
# print(aa_list)

# # filter() 사용
# def func(x):
#     if x%2 == 0:
#         return x
    
# b_list = list(filter(func, a_list))
# print(b_list)

# c_list = list(filter(lambda x:x%2==0, a_list))
# print(c_list)


# map 함수 관련
# a_list = [1, 2, 3, 4, 5]    # list 모든 값에 제곱을 해서 리스트를 생성
# aa_list = []
# for i in a_list:
#     aa_list.append(i**2)

# def func(x):
#     return x**2

# # map() 사용
# print(list(map(func, a_list)))       # map() => a_list 값을 하나씩 func 함수에 넣어서 값을 돌려줌

# # 람다식 - map() 함수를 lambda로 사용하면 코드를 줄일 수 있음
# print(list(map(lambda x:x**2, a_list)))



# def add(a, b):
#     return a + b

# print(add(10, 20))

# def func(a,b,c):
#     return max(a,b,c)   # max() : 3개의 값 중에 가장 큰 수를 찾아냄

# print(max(10, 5, 20))