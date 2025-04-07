# 클래스 : 변수, 함수 집합체 - 변수에 대한 그룹핑 필요 kor, eng, math...
# list, dict 타입 - 함수까지 sum, avg, rank..
# 입력 받을때 처리, 수정할때 직접 처리
# 특정 데이터 값이 들어왔을때 잘못된 데이터는 입력이 되지 않도록 구현


class Car:
    def __init__(self, color, tire, door):      # 생성자 __init__함수 사용
        self.color = color      # self.color : Car 변수, color : 요청 변수
        self.tire = tire
        self.door = door
        self.speed = 0
    
    # 속도 올리기
    def speedUp(self, s):
        self.speed += s
    def speedDown(self, s):
        self.speed -= s
# 생성자를 사용한 객체 선언 과 동시에 데이터 입력
c = Car("red", 4, 5)
c2 = Car("blue", 5, 5)
        


# class Car:
#     color = "white"
#     speed = 0
#     tire = 4
#     door = 5
    
#     # 속도 올리기
#     def speedUp(self, s):
#         self.speed += s
#     def speedDown(self, s):
#         self.speed -= s
        
# # 리스트 선언
# a_list = [1, 2, 3, 4, 5]
# # 리스트 값 입력
# a_list[0] = 50
# # 리스트 출력
# print(a_list)

# # 클래스 객체선언
# a = Car()
# # 클래스 변수에 값 입력 - 참조변수.변수명
# a.speed = 50
# # 클래스 변수 값 출력 - 참조변수.변수명
# print(a.speed)

# # 함수 사용방법 - 참조변수.함수명
# a.speedUp(20)
# print(a.speed)  # 70 출력

# a_list2 = [1, 2, 3, 4, 5]
# a_list2 = a_list    # 얕은 복사
# a_list2 = [*a_list] # 깊은 복사

# a = Car()       # 각각의 변수, 함수가 됨

# 기본형태 객체 선언 후 데이터 입력
# # red, 5, 4
# a2 = Car()      #  차 구매 후 색도 다시, 문짝도 달고, 타이어도 달고..
# a2.color = "red"
# a2.tire = 5
# a2.door = 4

# # blue, 5, 5 
# a3 = Car()
# a3.color = "blue"
# a3.tire = 5
# a3.door = 5