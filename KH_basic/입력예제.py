# 사용자에게 콘솔로 입력을 받아 변수에 대입
# input() 함수를 사용
# input() 함수는 문자열로 입력을 받음
"""
print("이름을 입력 하세요 : ")
name = input()
print(f"당신의 이름은 {name} 입니다.")
"""

# 정수 타입으로 변수에 값을 대입하기 위해서는 형 변환이 필요
"""
age = int(input("나이를 입력 하세요 : "))
print(age + 10)
"""

# 이름, 나이, 주소, 직업, 성적(실수 타입)float을 입력 받아 출력하기
"""
print("이름을 입력하세요 : ", end="")
name = input()
print(f"당신의 이름은 {name}입니다.")

print("나이를 입력하세요: ", end="")
age = int(input())
print(f"당신의 나이는 {age} 세 입니다.")

print("당신이 거주하는 장소의 주소를 입력하세요: ", end="")
addr = input()
print(f"당신이 거주하는 곳은 {addr}입니다.")

print("당신의 성적을 입력하세요: ", end="")
grade = float(input())
print(f"당신의 성적은 {grade}입니다.")
"""

"""
name = input("이름 입력: ")
age = int(input("나이를 입력 : "))
addr = input("주소 입력 : ")
job = input("직업 입력 : ")
score = float(input("성적 입력 : "))

print(f"안녕하세요? \"{name}\"님") # 코드 내에서
print(f"당신의 주소는 {addr}이고 직업은 {job}이고 나이는 {age} 입니다.")
print(f"당신의 성적은 {score:.2f} 입니다.")
"""

# 국어 영어 수학 과학 성적을 공백 기준으로 입력 받아 총점 구하기
#kor, eng, mat, scn = map(int, input("성적 입력 : ").split())
#print(f"총점 : {kor + eng + mat + scn}")
#print(f"평균 : {(kor + eng + mat + scn) / 4 } ")

"""
score = list(map(int, input("성적 입력 : ").split()))
print(f"총점 : {sum(score)}")
print(f"평균 : {sum(score) / len(score)}")
"""

# 24시간제 시간을 : 기준으로 입력 받아서 시, 분, 초로 찍는데 12시간제로 변환해서 출력
hour, min, sec = map(int, input("시:분:초 : ").split(":"))

if hour > 12:
    hour -= 12  # hour = hour - 12
    print(f"오후 {hour}시 {min}분 {sec}초")
else:
    print(f"오전 {hour}시 {min}분 {sec}초")