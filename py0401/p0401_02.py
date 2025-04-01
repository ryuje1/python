a_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

count = 0

while True:
    # 화면 출력
    print(a_list)
    
    # 숫자 입력
    num = int(input("숫자를 입력하세요.  "))
    for i in range(len(a_list)):    # len(a_list) = 5
        if a_list[i] == num:
            a_list[i] = "X"
            count += 1
            break
    
    # X개수 확인
    if count == 5:
        print("빙고 완성!!")
        print(f"개수 : {count}")
        break
    
    print(f"현재 X 개수 : {count}")