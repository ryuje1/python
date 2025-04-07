class Car:
    speed = 0
    tire = 4
    door = 5
    def speedUp(self, s):
        self.speed += s
        print("현재 속도 :", self.speed)
        
class Sedan(Car):   # Car를 상속
    color = "red"
    
c = Car()
# print(c.gireType)   # 없는 변수 출력 시 Error
s = Sedan()
print(s.tire)