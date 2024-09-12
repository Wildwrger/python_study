# 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 시급 : 9860원
# 야간 근무 시급 : 주간 시급 * 1.5
# [입력] 주간근무 [1] 야간근무 [2]를 입력하세요
# [입력] 근무시간을 입력 하세요 :
# [출력] print(f"{근무시간}시간 동안 근무한 {근무타입 문자열} 급여는 {급여}원 입니다.")

d_pay = int(9860)
n_pay = int(d_pay * 1.5)

work = int(input("주간근무 [1] 야간근무 [2]를 입력하세요 : "))
hour = int(input("근무시간을 입력하세요 : "))

if work == 1:
    work_str = "주간"
    pay = (d_pay * hour)
elif work == 2:
    work_str = "야간"
    pay = (n_pay * hour)
else:
    print("근무타입의 번호를 제대로 입력하여 주십시오.")
    exit()

pay_str = f"{pay:,.0f}"
print(f"{hour}시간 동안 근무한 {work_str} 급여는 {pay_str}원 입니다.")

