# 날짜 시간
# 날짜 클래스
import datetime # import - 다른 객체, 클래스를 갖다 쓰는 것

now = datetime.datetime.now()
# print("현재시간 :", now)

# print(now.year) # 연도만
# print(now.month) # 달만
# print(now.day) # 요일만
# print(now.hour) # 시간만
# print(now.minute) # 분만
# print(now.second) # 초만

# 시간이 12 이상이면 오후, 12 미만이면 오전이라고 시간을 출력하시오.
# 13시 -> 오후 1시
# 9시 -> 오전 9시

# 15시 - 오후 3시라고 출력

# if 조건을 사용해서 오전, 오후라고 하고 시간을 출력하시오.

hour = now.hour
min = now.minute

if hour > 12:
    print("오후 {:02d}:{:02d}".format(hour-12, min))
else:
    print("오후 {:02d}:{:02d}".format(hour, min))
    
# 2025-03-27
print("{}-{:02d}-{}".format(now.year, now.month, now.day))