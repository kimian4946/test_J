import random
# 알람시계 문제
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


# 사칙연산 문제
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


# 고양이
# print("\    /\ \n )  ( ')\n(  /  )\n \(__)|")
# 강아지
# print('|\_/|\n|q p|   /}\n( 0 )"""\\\n |"^"`   |\n ||_/=\\__|\n')

def sum(*ints):
    while True:
        A = int(input(" 입력 : ..."))
        if A % 4 == 0 and (A % 100 != 0 or A % 400 == 0):
            print(1)
        else:
            print(0)

        return ints
# sum()
# 오븐 시계
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


# def sum(*strs):
#     money1 = 10000
#     money2 = 1000
#     a=int(input("입력 하시오 . . ."))
#     b=int(input("입력 하시오 . . ."))
#     c=int(input("입력 하시오 . . ."))
#     if a == b == c:
#         money = money1+(a * 1000)
#         print(money)
#     else :
#         if a == b or a == c:
#             money_1 = money2 + (a * 100)
#             print(money_1)
#         elif b == a or b == c:
#             money_1 = money2 + (b * 100)
#             print(money_1)
#         elif a != b != c:
#             print(max(a, b, c)*100)
#         else:
#             print("Error")
#         return strs
# sum()


# word = "baekjoon"
# alpha = {'a':-1}
# for i in range(1, 26):
#     alpha[chr(97+i)] = -1

# for i in range(0, len(word)):
#     alpha[word[i]] = i

# print(alpha.values())


# n=int(input(">"))
# for i in range(n):
#     c=int(input(">"))
#     t=str(input(">"))
#     for i in t:
#         print(i * c ,end = '')


position = ['힌트1', '힌트2', '힌트3', '힌트4', '힌트5',
            '힌트6', '힌트7', '힌트8', '힌트9', '힌트10', '힌트11']
correct = {'사로 시작하는 동물': '사슴', '너무 빠르고 두 귀가 있는': '토끼', '스마트폰을 사용하는': '인간', '등에 가시가 있는': '고슴도치', '영화에 나오는 고슴도치': '소닉',
           '나무에 매달리는': '원숭이', '코가 긴': '코끼리', '힘을 좋은': '캥거루', '잠만 자는': '코알라', '군집생활': '개미', '날렵한 몸매': '고양이'}


hint = {'힌트1': '군집생활'}
hint['힌트2'] = '날렵한 몸매'
hint['힌트3'] = '나무에 매달리는'
hint['힌트4'] = '너무 빠르고 두 귀가 있는'
hint['힌트5'] = '스마트폰을 사용하는'
hint['힌트6'] = '사로 시작하는 동물'
hint['힌트7'] = '등에 가시가 있는'
hint['힌트8'] = '영화에 나오는 고슴도치'
hint['힌트9'] = '코가 긴'
hint['힌트10'] = '힘을 좋은'
hint['힌트11'] = '잠만 자는'

hint2 = {'개미': '작고 검정색'}
hint2['고양이'] = '세종대왕이 좋아했던'
hint2['원숭이'] = '옛날에 일본한테 받은 동물'
hint2['토끼'] = '호주에 약 1억마리가 있는 동물'
hint2['인간'] = '전세계에서 약 80억 명이 있는 동물'
hint2['사슴'] = '동물원 탑 티어에 들어가는 동물'
hint2['고슴도치'] = '소닉과 유사한 동물'
hint2['소닉'] = '?? 게임의 주인공'
hint2['코끼리'] = '코가 손이 동물'
hint2['캥거루'] = '호주 출신 조폭'
hint2['코알라'] = '잠만 자는 동물'


score = 0  # 한번에 맞추면 2점, 한번 틀리면 1점, 못맞추면 0점
while True:
    i = random.randint(0, len(position) -1 )
    j = hint.get(position[i])
    print('힌트:', j)
    if correct[j] == input("정답:"):
        print("정답입니다")
        score += 2
        print(score, "자신의 점수")

    else:
        print('힌트:', hint2.get(correct[j]))
        if correct[j] == input("정답:"):
            print("정답입니다")
            score += 1
            print(score, "자신의 점수")
        else:
            print("오답입니다")
            print(score, "자신의 점수")


# a = {1:'일'}
# a = {2:'이'}
# a = {3:'삼'}
# 3:'삼'

# a = {1:'일'}
# a[2] = '이'
# a[3]='삼'
# 1:'일',2:'이',3:'삼'

