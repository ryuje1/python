# 파일 입출력 : 파일 열기 - 파일 읽기, 파일 쓰기 - 파일 닫기
# 파일 열기 - 3가지 모드 => r : 읽기모드, w : 쓰기모드, a : 추가모드, b : 이진파일-파일복사
# f = open("a.txt", "r")  # 읽기모드
# f = open("a.txt", "w")  # 쓰기모드
# f = open("a.txt", "a")  # 추가모드


# news.txt 파일 출력하시오.
f = open("py0404/news.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
f.close()


# # 파일 읽어오기 - 절대경로
# # \\ 2개 또는 /
# f = open("C:/workspace/python/a.txt", "r", encoding="utf-8")
# # f = open("C:\\workspace\\python\\a.txt", "r", encoding="utf-8")
# f = open("py0404/b.txt", "r", encoding="utf-8")  # 폴더 안에 있는 파일 읽어오기

# 방법 1)
# for line in f:
#     print(line.strip())
# f.close()   # close() 하지 않으면 문제가 생길 수 있으니 꼭 해줘야함

# 방법 2)
# while True: # 3줄
#     line = f.readlines()
#     if not line: break
#     print(line.strip())
# f.close()

# # 파일 읽기 - readlines() : 모두 읽어오기
# f = open("a.txt", "r", encoding="utf-8")
# lines = f.readlines()   # 모두 읽어오기. 리스트 개념으로 뽑아와서 1줄씩 출력
# for line in lines:
#     print(line.strip())
# f.close()

# # 파일 읽기 - r 1줄 읽기 read()
# # 파일이 없으면 Error
# f = open("a.txt", "r", encoding="utf-8")
# print(type(f))
# # 모든 줄을 실행하기 위해 for문을 사용
# for line in f:
#     print(line.strip())     # strip() 공백제거
# f.close()