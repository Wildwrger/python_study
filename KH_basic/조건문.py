# 제어문이란? 조건문과 반복문을 의미
# num = int(input("정수값 입력 : "))
#
# if num > 100:
#     print(f"{num}은 100보다 큽니다.")
# elif num < 100:
#     print(f"{num}은 100보다 작습니다.")
# else:
#     print(f"{num}은 100과 같습니다.")

# 실습문제
# 성적을 입력받아서 0 ~ 100 사이가 아니면 성적을 잘못 입력 하였다고 표기
# 성적이 0 ~ 100이고,
# 90점 이상이면 A
# 80점 이상이면 B
# 70점 이상이면 C
# 60점 이상이면 D
# 나머지는 F

while True:
    score = int(input("성적을 입력하여 주십시오 : "))
    if 0 <= score <= 100 : break
    print("성적을 잘못 입력하셨습니다.")

if score >= 90: print("당신의 성적은 \"A\"입니다")
elif score >= 80: print("당신의 성적은 \"B\"입니다")
elif score >= 70: print("당신의 성적은 \"C\"입니다")
elif score >= 60: print("당신의 성적은 \"D\"입니다")
else: print("당신의 성적은 \"F\"입니다")


# 세자리 정수를 입력 받아 100의 자리, 10의 자리 , 1자리로 나누어 담고
# 이 중 가장 큰 수 출력
# 몫과 나머지로 변수 할당
# if ~ else 값 비고

# num = int(input("1000미만의 양수이자 정수를 입력하시오 : "))
#
# if 1000 > num >= 0:
#     a = (num // 100)
#     b = (num % 100) // 10
#     c = (num % 10)
#     if a > b and a > c: print("백의 자리의 정수가 가장 큽니다.")
#     elif b > a and b > c: print("십의 자리의 정수가 가장 큽니다.")
#     elif c > a and c > b: print("일의 자리의 정수가 가장 큽니다.")
#     else: print("백, 십, 일의 자리 정수 중 가장 큰 정수는 없습니다.")
#     print(a, b, c)
# else: print("조건을 만족하는 정수를 입력하여 주십시오.")

