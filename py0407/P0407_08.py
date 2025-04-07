class Student:
    # 인스턴스 변수 - 객체 선언시 각각 변수들이 존재, 공용으로 사용X
    # no = 1
    # name = ""
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0
    # rank = 0
    count = 1   # 클래스 변수 - 모든 객체가 공용으로 사용하는 변수 (클래스명.변수명 형태)
    
    # 생성자 함수
    def __init__(self, name, kor, eng, math):
        self.no = Student.count         # 인스턴스 변수
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = (kor + eng + math) / 3
        # self.avg = self.total / 3
        self.rank = 0
        Student.count += 1              # 객체 선언할 때마다 1 증가
        
    def __str__(self):      # 특별 함수
        return f"{self.no}, {self.name}, {self.kor}, {self.eng}, {self.math}, {self.total}, {self.avg}, {self.rank}"
        
class Students:
    def __init__(self):
        self.students = []
        
    def add(self, s):
        self.students.append(s)
        
    def __str__(self):      # 리턴은 무조건 문자열을 해줘야 함
        for s in self.students:
            print(s.no, s.name, s.kor, s.eng, s.math, s.total, s.avg, s.rank)    
        return ""

ss = Students()
s = Student("홍길동", 100, 100, 99)
s2 = Student("유관순", 90, 90, 91)
s3 = Student("이순신", 80, 80, 89)
ss.add(s)
ss.add(s2)
ss.add(s3)
print(ss)

        
# # 매개변수가 있는 생성자를 활용해서 데이터 입력
# s = Student("홍길동", 100, 100, 99)     # 매개변수가 있는 생성자 객체 선언
# print(s.no, s.name, s.kor, s.eng, s.math, s.total, s.avg, s.rank, Student.count)    # 2
# s2 = Student("유관순", 90, 90, 98)
# print(s2.no, s2.name, s2.kor, s2.eng, s2.math, s2.total, s2.avg, s2.rank, Student.count)    # 3
# print(s.no, s.name, s.kor, s.eng, s.math, s.total, s.avg, s.rank, Student.count)    # 3
# s3 = Student("이순신", 90, 91, 90)
# print(s3.no, s3.name, s3.kor, s3.eng, s3.math, s3.total, s3.avg, s3.rank, Student.count)    # 4



# a_list = [1, 2]

# s = Student()       # 기본 생성자
# s.name = "홍길동"
# print(s.no, s.name)

# s2 = Student()
# s2.no = 2
# s2.name = "이순신"
# print(s2.no, s2.name)