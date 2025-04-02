# 문자열

print('1234'.isdigit())     # 숫자인지 확인
print('abc'.isalpha())      # 알파벳인지 확인 - 한글 불가능
print('abc123'.isalnum)     # 글자 및 숫자인지 확인 - abc, a1, 123 모두 가능
print('abc'.islower())      # 모두 소문자인지 확인
print('ABC'.isupper())      # 모두 대문자인지 확인


# a = "1234"
# if a.isdigit(): # 숫자로 변환 가능한지 확인
#     print("숫자로 가능합니다.")

# my = int(input("숫자를 입력하세요.  "))     # 문자 입력 시 Error

# while True:
#     my_input = input("숫자를 입력하세요.  ")
#     if my_input.isdigit():
#         my_input = int(my_input)
#     else:
#         print("숫자가 아닙니다. 숫자를 입력하셔야 합니다.")

# # map(함수, 데이터 값)
# score = ['100', '99', '90']
# # 함수
# def cal(x):
#     return int(x)*100
# s_list = list(map(cal, score))
# print(s_list)

# zfill() : 10자리 공백은 0으로 채우라는 의미 (형식 : 변수.zfill(숫자))
# ss.zfill(10)

# s_list = list(map(int, score))  # 한번에 형변환 가능
# print(s_list)

# sum = 0
# for s in score:
#     # sum += s                # 문자열이라 단순붙여지기만 함
#     sum = sum + int(s)        # 형변환 str -> int
# print("합계 : {}".format(sum))

# txt = ","
# txt2 = txt.join("안녕")   # 안녕 사이에 txt(,)를 넣어줌
# print(txt)
# print(txt2)     # 안,녕 출력

# # 데이터베이스 (DB)는 리스트를 저장할 수 없음
# # 문자열로 저장 => split() 을 활용
# txt = "1,홍길동,100,100,100,300,100.0,1"
# txt_list = txt.split(",")
# print(txt_list)
# txt_list[1] = "유관순"
# print(txt_list)

# txt = "a, b, c, d, 안녕, 반가워"
# txt_list = txt.split(",")   # 쉼표 기준으로 구분하여 문자열 분리
# print(txt_list)             # ['a', ' b', ' c', ' d', ' 안녕', ' 반가워'] 출력

# txt = "   안녕하 세요  "
# # 문자열 대체
# # replace() : 문자를 다른 문자로 치환
# print(txt.replace(" ",""))  # 공백을 공백없이 변경
# txt2 = "파이썬 공부가 쉬워요~ 너무 쉬워요. 파이썬은 재미있어요."
# print(txt2.replace("파이썬","자바"))  # 자바 공부가 쉬워요~ 너무 쉬워요. 자바은 재미있어요. 출력

# txt3 = "----파---이썬 ----"
# print(txt3.strip("-"))  # strip() => 공백 뿐만 아니라 특정 글자도 제거 가능. 중간 글자는 제거 X
# print(txt3.replace("-", ""))    # 중간 글자까지 제거

# 공백 제거
# strip() : 앞뒤 공백 제거. 중간 공백은 제거X
# rstrip() : 왼쪽 공백 제거 / lstring() : 오른쪽 공백 제거
# print(txt.strip())


# txt = "파이썬 공부가 쉬워요~ 너무 쉬워요. 파이썬은 재미있어요."
# print(txt.count("파이썬"))  # 문자열의 검색하려고 하는 글자 개수 출력
# print(txt.count("요"))
# print(txt.find("공부"))     # 공부가 몇번째 위치하는지 찾아줌. (공백도 문자로 인식해서 4 출력)
# print(txt.find("자바"))     # 없을 때는 -1 출력

# t = "aaa.py"
# print(t.endswith("py"))     # 있으면 True, 없으면 False

# txt = "abBBcDd hello apple"         # 대소문자
# print(txt.upper())      # 전체 대문자 출력
# print(txt.lower())      # 전체 소문자 출력
# print(txt.swapcase())   # 대문자는 소문자로, 소문자는 대문자로 변경
# print(txt.title())      # 단어의 첫글자를 대문자로 변경


# txt = "안녕하세요"
# a_list = [1, 2, 3, 4, 5]

# print(a_list[1:3])    # 2, 3 출력 (1번째:3-1번째)
# print(txt[1:3])       # 녕하 출력
# print(txt[2:])        # 하세요 출력 (2번째:끝까지)
# print(txt[:3])        # 안녕하 출력 (처음부터:3-1번째)

# print(txt*3)          # txt 3번 출력
# print("-"*50)
# print(len(txt))       # 글자길이 출력

# print(txt[::-1])      # 글자 역순 출력

# # # 문자열도 index 번호를 가짐
# # print(txt[1])       # 녕 출력
# # print(a_list[1])    # 2 출력