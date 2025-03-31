# X좌표 : 1
# Y좌표 : 3
# 1,3 -> 문자 인식

# num1 = int(input("X 좌표 : "))
# num2 = int(input("Y 좌표 : "))
# print(f"[X, Y좌표 : {num1}, {num2}]")

num = input("X, Y 좌표 (0/10) : ")   # 1,3
n_list = num.split("/") # ""안의 문자를 기준으로 분리하라는 의미 (공백, \t, \n, @ ... 가능) 타입 = 문자열   **중요 외워두기
# CSV 파일 => 쉼표를 기준으로 분리 ex)공공데이터 파일
print(f"[X, Y 좌표 : {n_list}]")

