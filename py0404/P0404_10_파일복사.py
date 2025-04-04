# 문서 읽어오기 - r
# 일반파일 읽어오기 - rb (파일의 내용을 읽어오는게 아니라 파일 자체를 읽어옴)

f = open("py0404/a.jpg", "rb")  # 파일 읽기

# 이진파일은 용량이 클 수 있으므로, 1 byte 읽어오기
while True:
    fData = f.read(1)
    if not fData: break
f.close()
print("파일 읽어오기 완료")

# 문서 저장 - w, a
# 파일 저장 - wb
# 폴더 존재 확인 : os.path.exists()
# 폴더 생성 : os.makedir() : 폴더 1개 C:\\download1\\aaa\\a.jpg => aaa 못찾음
# 폴더 생성 : os.makedirs() : 모든 폴더 생성 C:\\download1\\aaa\\a.jpg
import os
# 폴더가 없으면 생성 후 진행
if not os.path.exists("C:\\download1"):
    os.makedirs("C:\\download1")

ff = open("C:\\download1\\b.jpg", "wb")     # 파일 쓰기
len = ff.write(fData)
print(f"파일크기 : {len} 바이트")
ff.close()

print("파일 저장 완료")