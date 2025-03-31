## 리스트 삭제 방법
# del - 해당 위치 값 삭제
a_list = [1, 2, 3, 4,5]
del a_list[2]
print(a_list) # [1, 2, 4, 5]

# pop - 맨 뒤 삭제, 특정 위치 삭제
a_list.pop()
print(a_list) # [1, 2, 4]

# remove - 데이터 값으로 삭제
a_list.remove(1)
print(a_list) # [2, 4]

# clear - 전체 삭제
a_list.clear()
print(a_list) # []



# ## 리스트 추가 방법
# # append - 마지막에 값 추가
# a_list = [1, 2, 3]
# a_list.append(4)
# print(a_list) # [1, 2, 3, 4]

# # insert - 특정 위치에 값 추가 (잘 사용하지 않음. 데이터 많으면 시간이 많이 걸리기 때문)
# a_list.insert(1, 100) # 1이라는 위치에 100을 넣으라는 의미. 기존 값은 뒤로 이동.
# print(a_list) # [1, 100, 2, 3, 4]

# # extend - 다른 리스트를 추가
# a_list.extend([100, 200, 300])
# print(a_list) # [1, 100, 2, 3, 4, 100, 200, 300]



# # 리스트 내포. append보다 약간 시간 빠름
# a_list = [i for i in range(1,11)]
# print(a_list)


# # 명령어 append => 리스트에 추가하는 방법
# a_list = []
# for i in range(1, 11):
#     a_list.append(i)
# print(a_list)


# # index 번호를 넣으려면 enumerate 사용
# a_list = [273, 10, 5, 9, 100, 1000, 50]
# for idx, value in enumerate(a_list): # enumerate => 인덱스 번호를 받을 수 있음
#     print(f"{idx+1} : {value}")      # 0번 부터 시작이라 idx+1