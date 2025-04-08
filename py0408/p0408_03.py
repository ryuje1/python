a = [10, 5, 2, 4, 7]
print(min(a))   # 최소값
print(max(a))   # 최대값
print(sum(a))   # 합계

a_dict = [ {"no":1, "name":"홍길동"}, 
           {"no":5, "name":"유관순"}, 
           {"no":3, "name":"이순신"}, 
           {"no":4, "name":"강감찬"}, 
           {"no":2, "name":"김구"} ]
# print(max(a_dict))  # 값 2개 비교해야해서 Error
print(max(a_dict, key=lambda x:x['no']))
print(max(a_dict, key=lambda x:x['name']))

a_dict.sort(key=lambda x:x['no'])   # 순차정렬
a_dict.sort(key=lambda x:x['no'], reverse=True) # 역순정렬
print(a_dict)


print(a.sort())
print(a.sort(), reverse=True)
print(a)