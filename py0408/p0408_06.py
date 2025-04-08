from stuModule import Student

s1 = Student("홍길동", 100, 100, 99)
s2 = Student("유관순", 100, 100, 80)

print(s1)   # class 객체에서 __str__ 함수

if s1 <= s2:    # 
    print("s1이 더 크거나 같습니다.")
else:
    print("s1이 작습니다.")


# # 변수의 if문 비교
# a = 10
# b = 20

# if a>b:
#     print("a가 더 큽니다.")
# else:
#     print("a가 작습니다.")