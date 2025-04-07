# 클래스 형태 - 파일 구성 : 다른 타입 형태를 넣을 수 있다는 장점

# 변수 -> 배열(같은 타입) -> 다른 타입(구조체) -> 객체(클래스) 변수, 함수를 같이 담는 형태로 발전
# 객체지향언어 -> 고급언어

# 클래스 장점
# - 변수, 함수 모두 포함
# - 변수에 대한 값을 확인·비교 가능
# - 캡슐화 : 변수에 직접 접근을 막을 수 있음


# class 첫 글자는 대문자 사용 (강제X 권장사항)
# 설계도
class Stu:
    # 생성자 - 클래스가 선언될때 데이터를 받아서 변수에 저장시켜주는 함수
    def __init__(self, no, name, kor, eng, math, total, avg, rank):
        self.no = no            # class 안에 변수가 선언됨
        self.name = name
        if kor>0 and kor<=100:  # 이 조건에 만족해야만 넣어짐
            self.kor = kor
        self.__eng = eng        # 직접적인 접근을 막을 수 있음
        self.math = math
        self.total = total
        self.avg = avg
        self.rank = rank
        
s = Stu(1, "홍길동", 100, 100, 100, 300, 100.0, 1)
s.eng = 200
print(s.eng)


# 클래스 선언 후 변수 선언을 해서 사용가능. (잘 안쓰는 방법)
# class Stu: pass

# s = Stu()   # 클래스 선언
# s.no = 1    # 각각 변수 선언
# s.name = "홍길동"   # 변수 선언
# s.kor = 100        # 변수 선언
# print(s.no)


# stu = [1, "홍길동", 100, 100, 100, 300, 100.0, 1]
# while True:
#     stu[2] = 300        # 리스트는 값을 바꿀 수 있음
#     print("1. 학생 출력")
#     choice = int(input("원하는 번호를 입력하세요.  "))
#     if choice == 1:
#         print(stu)