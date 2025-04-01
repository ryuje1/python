a_list = [["X", "X", "X", "X", "X"], [6, "X", 8, 9, 10]]

# 현재 리스트의 X 개수 확인
no = 0
for i in range(5):
    if a_list[0][i] == "X":
        no += 1
        
if no == 5:
    print("빙고 완성!!")
print(f"현재 [0]방의 X 개수 : {no}")

