# 자연수 A, B, C
# A * B * C를 했을때 등장하는 숫자 (0~9)의 개수를 세는 문제

# a, b, c = (input("자연수를 3개 입력하십시오 : ")).split()
# num = int(a) * int(b) * int(c)
# print(num)
# for i in range(0, 10):
#     print(str(num).count(str(i)))

# 실습 2번, 문자열 반전, 문자열을 입력 받아서 문자열 반전 출력
# ex) asdf => fdsa

in_str = input("반전을 시키고 싶은 문자 및 문자열을 입력하십시오 : ")
for i in range(len(in_str) -1, -1, -1 ):
    print(in_str[i], end="")
# reverse_str = in_str[::-1]
# print(reverse_str)