# 1. 딕셔너리 추가
# 없는 키값에 값을 넣으면 추가
dic = {}
dic['no'] = 1
dic['name'] = "홍길동"
dic['kor'] = 100
print(dic)

# -------------------
# 2. 딕셔너리 삭제
# del 키값
del dic['no']   # del 키값 입력 시 삭제
print(dic)

# -------------------
# 3. 딕셔너리 수정
# 있는 키값에 값을 넣으면 수정
dic['name'] = '이순신'
print(dic)

# -------------------
# 4. 딕셔너리 출력
print(dic)
# print(dic['total']) # 없는 키값을 입력하면 Error
print(dic.get('total')) # get() => 없는 키값을 입력하면 None 데이터를 출력

print(dic.keys())   # key값만 리스트 형태로 출력
print(dic.values()) # value값만 리스트 형태로 출력
print(dic.items())  # 튜플 형태로 출력 => [('name', '이순신'), ('kor', 100)]

# -------------------
# 전체 출력 - key, value 모두 출력
for i, value in enumerate(dic):     # key와 value 값을 줘서
    print(f"{i} : {value}")

# 키를 돌려줌
for key in dic:
    print(key)          # key 출력
    print(dic[key])     # 값 출력
    
# 존재하는지 확인
if 'name' in dic:
    print("키값이 존재합니다")

if 'no' in dic:
    print(f"no : {dic['no']}")
else:
    print("no 키는 존재하지 않습니다.") 



# # 딕셔너리 생성
# # {key값:value값, key값:value값, key값:value값} 형식
# dic1 = {1:"a", 2:"b", 3:"c"}
# print(dic1)

# students_list = [1, "홍길동", 100]              # 리스트 생성
# print(students_list)
# students = {"no":1, "name":"홍길동", "kor":100} # 딕셔너리 생성
# print(students)

# student1 = {"학번":1000, "이름":"홍길동", "학과":"컴퓨터학과"}
# print(student1)




# # 리스트 자리 수 출력
# number = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# ## 리스트 자리 수 출력
# ## 자리 수 : 3, 값 : 273
# ## 자리 수 : 3, 값 : 103
# ## 자리 수 : 1, 값 : 5

# for n in number:
#     value = n
#     length = len(str(n))    # 숫자를 문자열로 바꿔서 길이 확인
#     print(f"자리 수 : {length}, 값 : {value}")



# ## 100 이상의 숫자만 출력하시오
# ## 그리고 그 합을 구하시오.

# sum = 0
# for n in number:
#     # print(n, end=" ")
#     if n >= 100:
#         sum += n
#         print(n)
# print("합계 : {}".format(sum))