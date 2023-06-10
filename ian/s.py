
for i in range(0,2):
    SUBway=input("회원가입 / 로그인")
    if SUBway == '회원가입':
        
        password_IDS=input("설정 아이디 : ")
        while True:
            print("비밀번호는 숫자를 이용해 8자 이내로 만드시오.")
    
            password_SQS=input("설정 비밀번호 : ")
            
            a= len(password_SQS)
            if a < 8:
                if password_SQS.isdecimal:
                    print("끝")
                    break
                
                else:
                    print(password_SQS,"<--")                       
            else:
                print(a,"<--")               
                

                
                
                
    elif SUBway == '로그인':
        password_ID=input("아이디 : ")
        password_SQ=input("비밀번호 : ")
        if password_IDS == password_ID and password_SQS == password_SQ:
            print("로그인 성공!")
        else:
            print("로그인 실패!")