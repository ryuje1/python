i_list = [1, 2, 3, 4, 5, 1, 2, 10]
dic = {"no":1, "name":"홍길동", "kor":100, "eng":90, "math":80, "total":270}
print(dic)
txt_list = ['안녕', '반가워', '다음', '내일', '봐', '잘', '지내', '봐요']

# ----------------------------
# 얕은 복사, 깊은 복사
new_list = i_list       # 얕은 복사 : new_list 값을 변경하면 i_list도 같이 변경됨 => 문제가 생길 수 있음
new_list2 = [*i_list]   # 깊은 복사 : new_list 값을 변경해도 i_list는 변경되지 않음 => new_list 따로 i_list 따로 별개임


# # zip
# for i, t in zip(i_list, txt_list):
#     print(i, t)     # 2개 리스트를 동시에 뽑아서 출력
    
# # zip 사용해서 list 생성
# new_list = list(zip(i_list, txt_list))  # 리스트 타입으로 변경 => 리스트 형태로 출력 []
# print(new_list)
# # [(1, '안녕'), (2, '반가워'), (3, '다음'), (4, '내일'), (5, '봐'), (1, '잘'), (2, '지내'), (10, '봐요')] 출력

# # zip 사용해서 dict 생성
# new_dic = dict(zip(i_list, txt_list))   # 딕셔너리 타입으로 변경 = > 딕셔너리 형태로 출력 {key:value}
# print(new_dic)
# # {1: '잘', 2: '지내', 3: '다음', 4: '내일', 5: '봐', 10: '봐요'} 출력
# # 중복된 값은 덮어씌움 (수정) => 뒤에 값만 남음


# # 리스트 내포
# # 1-10 까지 리스트 생성
# a_list = [i+1 for i in range(10)]
# print(a_list)
# a_list = [i for i in range(1, 11)]
# print(a_list)

# b_list = [0]*10     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 리스트 생성
# # append로 추가하는 것보다 0으로 된 리스트 생성하는게 속도가 더 빠름
# print(b_list)

# c_list= [i for i in range(1, 51) if i%2==1]     # i = 결과값을 넣어주는 값. for문에 대한 if조건문 1개까지 작성 가능. 파이썬만 가능
# print(c_list)


# # 딕셔너리 전체 출력
# for k in dic:   # dic 에 있는 모든 key 값
#     print(dic[k])   # key를 넣어서 value 값 출력

# for k, v in dic.items():
#     print(k, v)     # key, value 값 동시 출력
    
    
# # 리스트 전체 출력
# for i in list:
#     print(i)


# # 딕셔너리 정렬
# import operator
# dic_sort = sorted(dic.items(), key=operator.itemgetter(0))  # key값을 가지고 정렬
# print(dic_sort)

# # 리스트 정렬
# list.sort() # 리스트 순차정렬
# print(list)
# list.sort(reverse=True) # 리스트 역순정렬
# print(list)


# # # 딕셔너리 key, values 출력
# # print(dic.keys())   # key 값 출력       리스트 형태로 출력 => dict_keys(['no', 'name'])
# # print(dic.values()) # value 값 출력     리스트 형태로 출력 => dict_values([1, '홍길동'])
# # print(dic.items())  # key, value 동시에 출력    튜플 형태로 출력 => dict_items([('no', 1), ('name', '홍길동')])

# if 'no' in dic: # 딕셔너리를 비교할때 key를 가지고 비교하게 됨
#     print("있습니다.")

# # 딕셔너리 개별 출력
# print(dic['no'])
# # print(dic['kor'])       # 키가 없는 것을 출력할때 Error
# print(dic.get('kor'))   # get() 함수 사용 시 없는 키는 None 출력

# # 리스트 개별 출력
# print(list[0])


## 딕셔너리/리스트 수정, 삭제, 추가 **중요 외워두기~~ ##

# # 딕셔너리 수정
# dic['name'] = "유관순"
# print(dic)

# # 리스트 수정
# list[0] = 100
# print(list)

# # 딕셔너리 삭제
# del dic["no"]
# print(dic)

# # 리스트 삭제
# del list[0]
# print(list)

# # 딕셔너리 추가
# dic['kor'] = 100
# print(dic)

# # 리스트 추가
# list.append(100)
# print(list)