# 회원 가입을 위한 ID, PW 입력 받기
id = input("아이디 입력 : ")

if len(id) >= 8:
    pw = input("비밀번호 입력 : ")
    if len(pw) < 8 or len(pw) > 16:
        print("비밀번호는 8자리에서 16자리까지만 가능합니다.")
    elif pw.find(id) >= 0:   #   비밀번호 만들때 id의 문자열을 포함하는 경우
        print("비밀번호에 아이디를 포함 할 수 없습니다.")
    else:
        print(f"아이디 : {id}")
        print(f"비밀번호 : {pw}")
else:
    print("아이디는 반드시 8자리 이상이어야 합니다.")