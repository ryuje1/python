## 리스트 내포 100개 리스트의 값에 전부 +100 해서 출력하시오.
## [100, 101, 102, 103 ... 199 ]

arr = [i for i in range(100)]   # 0-99
print(arr)

arr2 = [i+100 for i in arr]
# arr2 = [i+100 for i in range(100)] 도 가능
print(arr2)

a_list = []
for i in range(100):
    a_list.append(i)
print(a_list)
# = a_list = [i for i in range(100)]    print(aa_list) 와 동일


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # arr2 = [1, 2, 3, 4, 5 ... 100]

# # 리스트 내포 - list 내에 for문이 존재 (파이썬만 가능, 리스트로 받을 수 있다는 장점)
# arr2 = [i+1 for i in range(100)]
# print(arr2)

# a_list = [1, 2, 3]
# aa_list = ["1m", "2m", "3m"]

# aaa_list = [str(i)+"m" for i in a_list] # i와 "m"은 다른 타입이라 i를 str타입으로 변환
# print(aaa_list)


# # arr2 리스트에 cm을 붙여서 리스트
# arr2_list = [str(i)+"cm" for i in arr2]
# print(arr2_list)
# # 파이썬만 가능

# arr3_list = []
# for i in arr2:
#     arr3_list.append(str(i)+"cm")
# print(arr3_list)
# # 위의 방법과 동일