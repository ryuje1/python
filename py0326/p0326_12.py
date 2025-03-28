a = 5; b = 3
print(a+b, a-b, a*b, a/b, a//b, a%b, a**2)
print("{:.2f}".format(a/b))

print(2+2-(2*2/2*2))  # 헷갈리니까 괄호 꼭 넣기

c = "안녕"
d = 5
e = 6
f = "감사"

# print(c+d) # 타입이 다르면 +연산자 불가능
print(c,d)
print(c+f)
print(d+e)

num = "10"
num2 = 5
print(int(num)+num2) # print(num+num2) 는 오류 발생, 문자열을 int로 타입 변경 후 더해야함