
n = int(input("정수를 입력하여 주십시오 : "))
for i in range(0 , n):  # 행의 개수
    for j in range(0,i+1):
        print("*", end="")
    print()
