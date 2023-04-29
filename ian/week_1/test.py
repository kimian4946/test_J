#알람시계 문제
# hour = int(input("시간을 입력하세요:"))
# minute = int(input("분을 입력하세요:"))

# print(hour,"시",minute,"분")

# if minute < 45 :
#     if hour == 0 :
#         hour = 24
#     hour = hour - 1
#     minute = minute + 60
# minute  = minute - 45
# print(hour,"시",minute,"분")
# print("\\ \' \" ")


#사칙연산 문제
# A = int(input("A 의 값"))
# B = int(input("B 의 값"))
# S = A + B
# print(S)
# D = A - B
# print(D)
# F = A * B
# print(F)
# G = int(A / B)
# print(G)
# H = A % B
# print(H)


#고양이 
# print("\    /\ \n )  ( ')\n(  /  )\n \(__)|")
#강아지
# print('|\_/|\n|q p|   /}\n( 0 )"""\\\n |"^"`   |\n ||_/=\\__|\n')

def sum(*ints):
    while True:
        A = int(input(" 입력 : ..."))
        if A % 4 == 0 and (A % 100 != 0 or A % 400 == 0) :
            print(1)
        else:
            print(0)
    

        return ints
# sum()
#오븐 시계
# hour=int(input("  시  "))
# minute=int(input("  분  "))
# c=int(input(" 추가 "))
# d = minute + c
# if d > 60:
#     minute = d % 60
#     hour  =  hour + int(d/60)
#     if hour == 24 :
#         hour = 0
# print(hour, '시', minute, '분')


def sum(*strs):
    money1 = 10000
    money2 = 1000
    a=int(input("입력 하시오 . . ."))
    b=int(input("입력 하시오 . . ."))
    c=int(input("입력 하시오 . . ."))
    if a== b == c:
        money = money1+(a * 1000)
        print(money)
    elif a == b or a == c or b == a or b == c or c == a or c == b:
        money_1 = money2 + (a * 100)
        print(money_1)
    elif a != b != c:
        print(max(a, b, c)*100)
        return strs
    else:
        print("Error")
sum()