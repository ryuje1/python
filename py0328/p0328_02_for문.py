# for문 반복문
# for i(값을 받을 변수) in range(반복 횟수(~ 또는 ~,~)) 또는 리스트 타입

# range(3) -> 0, 1, 2 총 3번 반복
for i in range(3):
    print("안녕하세요.")
    
for i in range(1, 4): # 1부터 4 앞까지 반복하라는 의미. 1, 2, 3 총 3번 반복. 만약 1부터 5까지 반복 원하면 (1, 6)
    print("안녕하세요.", i)
    
for i in range(1, 3+1): # 1, 4와 같은 의미
    print("안녕하세요.", i)
    
# range(1, 11, 5) => 1 : 시작번호, 11 : 마지막번호-1 만큼, 5 : 간격. 1부터 10까지 5 간격으로 반복하라는 의미.
for i in range(1, 11, 5):
    print("안녕", i)
    

# range 자리에 list 타입도 가능
a_list = [1, 2, 3, 4, 5]
for i in a_list:
    print("안녕", i)