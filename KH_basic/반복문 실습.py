# 양의 정수 n을 입력 받아 3 * 3 크기의 행렬을 출력하는 프로그램 작성
# 이 때 행렬의 값은 1부터 시작하여 왼쪽에서 오른쪽, 위애서 아래 순서대로 채워넣음
# 입력 : 3 * 3
# 1 2 3
# 4 5 6
# 7 8 9

# 1. 입력 받은 값으로 실제 출력 범위 정해야 함
# 2. 줄바꿈에 대한 처리
# 3. 줄맞춤

n = int(input("양의 정수 n을 입력해 주십시오: "))
for i in range(1, n * n + 1):
    print(f"{i:3}", end= " ")
    if i % n == 0: print()


