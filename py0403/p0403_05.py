## 로또 프로그램
import random
# 6개 숫자 랜덤 번호 생성
# 6개 입력한 번호 생성
# 당첨번호 확인
# 출력
# p0403_04.py 연습
## X 표시만 안됨.........

my_lotto = [0]*6
win_lotto = []
lotto = [i+1 for i in range(45)]    # 1-45
lotto2 = [i+1 for i in range(45)]

def lotto_mix():
    global lotto, lotto2
    random.shuffle(lotto)   # 번호 랜덤섞기

lotto_mix()
while True:
    print("[ 로또 프로그램 ]")
    print("-"*60)
    print("1. 로또 프로그램 재실행")
    print("2. 로또 번호 입력")
    print("3. 로또 당첨 확인")
    print("4. 로또 번호 리스트")
    print("5. 내가 입력한 로또 번호 확인")
    print("0. 프로그램 종료")
    print("-"*60)
    choice = int(input("원하는 프로그램 번호를 입력해주세요.  "))
    
    if choice == 1:     # 로또 프로그램 재실행
        lotto_mix()
    
    elif choice == 2:   # 로또 번호 입력
        count = 0   # 로또 번호 입력 개수
        while True:
            print("[ 로또 번호 입력 ]")
            print("-"*60)
            
            # 로또 순번 출력
            for i in range(45):
                if i%7 == 0: print()
                print(lotto[i], end="\t")
            print()
            # ------------
            
            choice = int(input("로또 번호를 입력해주세요.  (0. 이전화면)  "))
            if choice == 0 : break
            
            if choice < 0 or choice > 45:
                print(f"{choice}번은 없는 번호 입니다. 다시 입력해주세요. ")
                continue        # 재실행
            
            temp = 0
            for i in lotto2:
                if i == choice:
                    lotto2[i-1] = "X"   # i-1 이유?
                    my_lotto[count] = choice    # append와 동일. append 보다 속도 빠름. my_lotto에 choice 값 입력
                    count += 1          # 로또번호 입력개수 증가
                    temp = 1            # 존재하는지 확인
                    
            if temp == 0:
                print(f"{choice}번은 이미 입력하신 번호입니다. 다시 입력해주세요.")
                
            if count >= 6:
                print("로또번호 6개를 다 입력하셨습니다.")
                break

    elif choice == 3:   # 로또 당첨 확인
        for i in lotto[:6]:
            for j in my_lotto:
                if i == j: win_lotto.append(i)

        print("[ 로또 당첨 확인 ]")
        print("-"*60)
        print("당첨번호 :", lotto[:6])
        print("내가 입력한 번호 :", my_lotto)
        print("당첨된 로또 번호 :", win_lotto)
        print("당첨 개수 :", len(win_lotto))
    elif choice == 4:   # 로또 번호 리스트
        print("[ 로또 번호 리스트 ]")
        print("-"*60)
        print(lotto)
        print()
    elif choice == 5:   # 입력한 로또 번호 확인
        print("[ 입력한 로또 번호 확인 ]")
        print("-"*60)
        print(my_lotto)
        print()
    else:
        print("[ 프로그램 종료 ]")
        break
    