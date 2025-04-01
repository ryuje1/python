n_list = ['홍길동', '유관순', '이순신', '강감찬', '김구']
t_list = [100, 99, 89, 79, 69, 100]
a_list = [10.0, 9.0, 8.0, 7.0, 10.0]

# zip() : 2개 리스트를 합쳐서 1개 리스트로 나타냄. list 또는 dic 타입으로 변경 가능. zip으로 묶으면 튜플 형태()로 나타냄
print(list(zip(n_list, t_list, a_list)))    # zip만 하면 object 형태라서 list 형태로 변경해서 출력
print(dict(zip(n_list, t_list)))
# list 타입은 리스트 3개도 가능하나 딕셔너리 타입은 key:value 2개의 값만 가능해서 3개는 불가능

# 튜플 => () 값 수정불가 / 리스트 => [] 값 수정가능 값 수정가능 유무 빼고 똑같음
# 딕셔너리 {} 값 수정가능
# tuple_list = list(zip(n_list, t_list))


# students = {"no":1, "name":"홍길동", "kor":100}
# # for i, v in enumerate(students):    # enumerate() i => 키값이 아니고 인덱스 값을 받음. 0, 1, 2... 아래대로 해야함
# for key, value in students.items():   # key값 : value값 출력
#     print(f"{key} : {value}")


# # 2개의 리스트 한번에 출력 가능
# n_list = ['홍길동', '유관순', '이순신', '강감찬', '김구']
# t_list = [100, 99, 89, 79, 69, 100]
# for n, t in zip(n_list, t_list):    # zip => 2개의 리스트 묶어서 전달
#     print(f"{n} : {t}")


# # 리스트내포 : if조건절을 넣을 수 있음. 단, 1줄만 가능 (2줄짜리는 불가능)
# n_list = [i for i in range(1, 51) if i%2==1]    # 1-50 중 홀수만
# # n_list = [i for i in range(1, 51) if i%3==0]    # 1-50 중 3의 배수만
# print(n_list)


#list = [1, 2, 3, 4, 5]

# # list2 = [101, 102, 103, 104, 105]
# list2 = [i+100 for i in list]   # 리스트내포. list+100
# print(list2)

# # list2 = ['10,100', '10,200', '10,300', '10,400', '10,500']
# # list+100*100, 1000단위 표시
# # format 함수 1000단위 표시 - :,d
# list2 = ["{:,d}".format((i+100)*100) for i in list]     # **중요 외우기~~~
# print(list2)


# --------------------------------
# # set => 중복을 제거해서 키를 확인
# myset1 = {1, 2, 2, 3, 3, 3, 5, 5, 7}
# print(myset1)

# menu_list = ['삼각김밥', '바나나우유', '삼각김밥', '사과', '바나나우유', '도시락', '삼각김밥']
# print(set(menu_list))  # list 타입을 set 타입으로 변경해서 확인. 종류 확인 가능