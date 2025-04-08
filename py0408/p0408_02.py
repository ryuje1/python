a = "홍길동님! 안녕하세요. 반갑습니다. 안녕 반가워. 안녕안녕"
## a.find()와 for문을 사용해서 안녕이 몇 번 나오는지 개수 출력하시오.

i = 0
count = 0
while True:
    num = a[i:].find("안녕")
    if num != -1:   # 안녕이라는 글자가 있는 경우
        count += 1  # 개수 1 증가
        i += num+1
    else: break
print("개수 :", count)

# 위치 찾고 +1 위치부터 다시 찾아서 개수 확인 (find() : 결과 값을 못 찾으면 -1 반환)
# print(a[0:].find("안녕"))
# print(a[0+6+1:].find("안녕"))
# print(a[0+6+1+13+1:].find("안녕"))
# print(a[0+6+1+13+1+7+1:].find("안녕"))
# print(a[0+6+1+13+1+7+1+1+1:].find("안녕"))
    

# num = a.count("안녕")   # count 함수
# print(num)
# print(a.count("안녕",0,len(a)))



# 글자가 있는지 확인
# if "안녕" in a:
#     print("안녕이라는 글자가 있습니다.")

# 글자가 있으면 위치를 알려줌
# print(a.find("안녕"))