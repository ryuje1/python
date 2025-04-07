class Student:
    phone = ""          # 인스턴스 변수 - 객체변수 : 각각의 객체별로 사용되는 변수
    address = ""
    count = 1           # 클래스 변수 사용 - 모든 객체가 공용으로 사용되는 변수
    
    def __init__(self, name, kor, eng, math):
        self.no = Student.count     # 클래스 변수
        Student.count += 1
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = self.total / 3
        self.rank = 0
    
    def s_total(self):    # 클래스 내의 함수는 무조건 self 입력
        self.total = self.kor + self.eng + self.math
    def s_avg(self):
        self.avg = self.total / 3
    def s_print(self):
        print(self.no, self.name, self.kor, self.eng, self.math, self.total, self.avg, self.rank)
        
# 객체 선언 (변수의 생성자 호출과 동일)
# no 번호를 부여하지 않음 => 1
print("1. 클래스 변수 :", Student.count)
s = Student("홍길동", 100, 100, 99)
print("2. 클래스 변수 :", Student.count)
s.s_print()
# no 번호를 부여하지 않음 => 2
s2 = Student("유관순", 90, 90, 91)
print("3. 클래스 변수 :", Student.count)
s2.s_print()
s3 = Student("이순신", 80, 80, 88)     # 번호 3 부여
s3.s_print()

s.kor = 50
s.s_total()
s.s_avg()
s.s_print()

# print("학생 :", s.no, s.name, s.kor, s.eng, s.math, s.total, s.avg, s.rank)