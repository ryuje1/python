## 중요중요 꼭 꼭 외워두기~~~~~

list = ["NCT 127", "김도영", "아이유", "NCT WISH",
        "NCT 127", "NCT WISH", "NCT 127", "김도영", "김도영",
        "NCT 127", "NCT 127", "NCT 127", "김도영", "김도영",
        "아이유", "아이유", "아이유", "아이유", "아이유",
        "NCT 127", "김도영", "NCT 127", "김도영", "김도영",
        "NCT 127", "NCT 127", "NCT 127", "NCT WISH", "김도영",] 

singer = {}
## 각각의 가수가 몇 번 존재하는지 출력하시오
## "NCT 127" : 6

# 숫자 형태 출력
for i in list:  # list에 있는 값을 1개씩 빼와서
    if i not in singer: # singer에 존재하는지 확인. 없을때
        singer[i] = 1
    else:
        singer[i] = singer[i] + 1   # singer[i] += 1 과 동일. 갯수 추가

for i, v in singer.items():  # (key, value) 형태. 튜플 형태로 가져옴. for i, v in enumerate(singer): 와 동일
    print(f"{i} : {v}")
        
# # 그래프 형태 출력
# for i in list:
#     if i not in singer:
#         singer[i] = ""
#     singer[i] += "♥"
# for i, s in enumerate(singer):
#     print(f"{i} : {singer[s]}")


# list = [1, 2, 3, 1, 2, 3, 5, 6, 8, 9, 10, 1, 2]
# dic = {}

# for i in list:
#     # dic에 추가 전에 dic에 키가 존재하는지 확인
#     if i not in dic:    # dic에 없으면 추가
#         dic[i] = 0
#     dic[i] = dic[i] + 1 # 키가 몇 개 존재하는지 개수 파악
#     # dic[i] += "■"

# # 픽토그램 그래프 형태로 출력
# for i, d in enumerate(dic):
#     print(f"{i} : {dic[d]}")

# print(dic)
        
# dic = {1:3, 2:3, 3:2, 5:1, 6:1, 8:1, 9:1, 10:1}