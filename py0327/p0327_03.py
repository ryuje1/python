# 학생 성적 프로그램
# 이름, 국어 성적, 영어 성적, 수학 성적을 입력받아 합계와 평균을 출력하는 프로그램을 구현하시오.

name = input("이름을 입력해주세요. ")
kor = int(input("국어 성적을 입력해주세요. "))
eng = int(input("영어 성적을 입력해주세요. "))
mat = int(input("수학 성적을 입력해주세요. "))
total = kor + eng + mat
avg = total / 3

print()
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print(f"{name}\t{kor}\t{eng}\t{mat}\t{total}\t{avg:.2f}")
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name, kor, eng, mat, total, avg))

# 계속 알아두기~~~~