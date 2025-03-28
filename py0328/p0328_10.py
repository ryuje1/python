fruits = ['사과', '배', '딸기', '바나나', '멜론']

# enumerate : index 번호를 받을 수 있음 => 데이터 분석할때 많이 씀 **알아두기
# 1. 사과
# 2. 배
# ...
for i, fruit in enumerate(fruits):
    if len(fruits)-1 != i:
        print("{}.{}".format(i+1,fruit), end=", ")
    else:
        print("{}.{}".format(i+1,fruit), end="")
    # 맨 마지막 번호는 쉼표 붙이지 않음
    
    
    
# scores = [65, 90, 100, 100, 50]

# for score in scores:
#     print(score, end=",")