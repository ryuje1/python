# 카드 프로그램 - Card 객체 사용
# p0403_03.py 참고
## 카드모양 : SPADE-4, DIAMOND-3, HEART-2, CLOVER-1
## 번호 1-A, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11-J, 12-Q, 13-K

class Card:
    def __init__(self, shape, number):
        self.shape = shape
        self.number = number
    
    def __str__(self):
        pass
        # return f"{self.shape}"
    
class CardFunc:
    pass
    # 함수
    
# cardMain.py
# 카드리스트 객체 호출
# 카드 객체 호출 45장
# 각각 5장을 나눠준 다음 비교해서 큰 수가 승리하는 형태로 구현