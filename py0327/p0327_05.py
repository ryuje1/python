# 조건문 if, if ~ else, if ~ elif ~ else (elif는 여러 번 사용 가능)
# 3가지 조건
# 음수, 0, 양수

# num = int(input("숫자를 입력해주세요. ")) 

# if num > 0:
#     print("양수 입니다.")
# elif num == 0:
#     print("0 입니다.")
# else:
#     print("음수 입니다.")


# 시험 성적을 입력받아
# 60점 이상이면 합격, 60점 미만 불합격
# score = int(input("성적을 입력하세요. "))

# if score >= 60:
#     print("합격 입니다.")
# else:
#     print("불합격 입니다.")
    

# 70점 이상 합격, 69~60점 재시험, 60점 미만 불합격
# score = int(input("성적을 입력하세요. "))

# if score >= 70:
#     print("합격 입니다.")
# elif score >= 60: # 69 >= score >= 60: 와 동일
#     print("재시험 입니다.")
# else:
#     print("불합격입니다.")


# 시험 -> 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 나머지 F
# 100~97점 A+, 96~93 A, 92~90 A-, 89~87 B+, 86~83 B, 82~80 B-
score = int(input("점수를 입력하세요. "))

if score >= 90:
    print("A", end="")
    if score >= 97: print("+") # 한줄이면 붙여쓰기 가능. 두줄이상 불가능
    elif score >= 93: pass # 아무것도 하지 않고 그냥 지나가겠다는 의미. 아무것도 안쓰면 Error
    else: print("-") # 여기 도달하면 if문 전체를 빠져나옴.
elif score >= 80:
    print("B", end="")
    if score >= 87: print("+")
    elif score >= 83: pass
    else: print("-")
elif score >= 70:
    print("C", end="")
    if score >= 77: print("+")
    elif score >= 73: pass
    else: print("-")
elif score >= 60:
    print("D", end="")
    if score >= 67: print("+")
    elif score >= 63: pass
    else: print("-")
else:
    print("F")

# print("안녕", end="") # print() 기본적으로 줄바꿈 되지만 end="" 사용하면 줄바꿈을 하지 않음
# print("하세요")