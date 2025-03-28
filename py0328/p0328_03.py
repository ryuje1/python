# 반복문을 사용해서 1-10까지 출력

# for i in range(1, 11):
#     print(i)
    

# AND, OR 연산자
# 모두 True여야 출력 / 둘 중 하나만 True여도 출력
# a = 10
# if a<9 and a>5: # False => 출력X
#     print(a)
    
# if a>5 or a<9: # True => 출력됨
#     print(a)
    
# a_list = [1, 2, 3, 4, 5]
# print(a_list[2]) # 3 출력
# print(a_list[1:4])  # 슬라이싱 : 여러 개를 한번에 출력. [시작위치:끝나는위치-1] => 2, 3, 4 출력 **중요
# print(a_list[:3])   # [:끝나는위치-1] - 처음부터 출력하라는 의미 => 1, 2, 3 출력
# print(a_list[2:])   # [시작위치:] - 시작위치부터 끝까지 출력하라는 의미 => 3, 4, 5 출력
# print(a_list[::2])  # 2개씩 증가해서 출력하라는 의미 => 1, 3, 5 출력
# print(a_list[::3])  # 3개씩 증가해서 출력하라는 의미 => 1, 4 출력
# print(a_list[::-1]) # 역순으로 출력하라는 의미 => 5, 4, 3, 2, 1 출력 **중요
# print(a_list[:-1])  # 마지막 한칸 바로 앞까지 출력하라는 의미 => 1, 2, 3, 4 출력 **중요

# a = "안녕하세요"
# print(a[2]) # 하 출력
# print(a[1:4]) # 녕하세
# print(a[:3]) # 안녕하
# print(a[2:]) # 하세요
# print(a[::-1]) # 요세하녕안
# print(a[:-1]) # 안녕하세

# print(a[:7]) # 슬라이싱은 에러 발생 X
# print(a[7]) # 인덱싱 없는 것 출력 시 IndexError.

# len()
# print(len(a_list))  # 리스트 갯수 확인
# print(a_list[:len(a_list)-1]) # 마지막 한칸 바로 앞까지 출력
# print(len(a))       # 문자열 길이 확인
# print(a[:len(a)])   # 문자열 몇개인지 모를때 처음부터 끝까지 출력하고 싶으면 이런 식으로 작성

# a_list[1:11:2] => 의미는 같으나 리스트타입은 :으로 range는 ,로 구분
# for i in range(1, 11, 2):
#     print(i, end=",")    # end="" 줄바꿈 없이 옆으로 출력. "" 사이에 쉼표 넣으면 i 사이 쉼표 넣어서 출력됨
    
# sum = 0
# for i in range (1, 100+1):  # 1에서 100까지 반복
#     sum = sum + i
# print("합계 : {}".format(sum))
# ** 이 형식은 외워두면 좋을듯


## 합계가 100 넘는 위치의 숫자는 얼마일까요?
## 1+2+3+4+5+6+7+8+ ... 합계가 100이 넘는 위치가 어디인지 출력하시오. 그 때의 값도 출력하시오.

sum = 0
i = 0   # i도 for문 바깥에 선언하기를 권장
for i in range (1, 100+1):  # if문과 동일하게 for문도 들여쓰기 중요
    sum = sum + i
    print("i : {}, sum : {}". format(i, sum))
    if sum >= 100: break

print("sum이 100 넘었을 때 i값 : ", i)
print("합계가 100이 넘었을때 sum값 : ", sum)