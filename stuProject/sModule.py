# class 2개 생성

class Student:
    count = 1
    def __init__(self, name, kor, eng, math):       # 생성
       self.no = Student.count
       self.name = name
       self.kor = kor
       self.eng = eng
       self.math = math
       self.total = kor + eng + math
       self.avg = self.total / 3
       self.rank = 0
       Student.count += 1
    
    def __str__(self):                              # 출력 형식
        return f"{self.no}, {self.name}, {self.kor}, {self.eng}, {self.math}, {self.total}, {self.avg}, {self.rank}"

class Students:
    def __init__(self):
        self.students = []
        
    def add(self, s):
        self.students.append(s)
        
    def __str__(self):
        for s in self.students:
            print(s.no, s.name, s.kor, s.eng, s.math, s.total, s.avg, s.rank)
        return ""