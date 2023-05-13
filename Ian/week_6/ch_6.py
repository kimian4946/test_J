






# def intsum(*ints):
#     sum = 0
#     for num in ints:
#         sum += num
#     return sum

# print(intsum(1, 2, 3))
# print(intsum(5,7, 9,11, 13))
# print(intsum(8,9,6,2,9,7,5,8))

# def calcstep(begin, end, step):
#     sum = 0
#     for num in range(begin, end + 1, step):
#         sum += num
#     return sum

# print("1 ~ 10 = ", calcstep(1, 10, 2))
# print("2 ~ 10 = ", calcstep(2, 10, 2))

# def calcstep(begin, end, step = 3):
#     sum = 0
#     for num in range(begin, end + 1, step):
#         sum += num
#     return sum

# print("1 ~ 10 = ", calcstep(1, 10, 1))
# print("1 ~ 100 = ", calcstep(1, 100))

# def calcstep(begin, end, step):
#     sum = 0
#     for num in range(begin, end + 1, step):
#         sum += num
#     return sum

# print("3 ~ 5", calcstep(3 , 5, 1))
# print("3 ~ 5", calcstep(begin = 3, end = 5, step= 1))
# pr
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# int("3 ~ 5", calcstep(step=1,end = 5,begin=3))
# print("3 ~ 5", calcstep(3, 5, step=1))
# print("3 ~ 5", calcstep(3, step= 1,end = 5))

# def kim():
#     temp = '김과장의 함수'
#     print(temp)

# kim()
# print()

# def kim():
#     temp = '김과장의 함수'
#     print(temp)


# def lee():
#     temp = 2 ** 10
#     print(temp)


# def pack(a):
#     temp = a * 2
#     print(temp)



# kim()
# print(lee())
# pack(6)

# salerate = 0.9

# def kim():
#     print("오늘의 할인율: " , salerate)

# def lee():
#     price = 1000
#     print("가격 : ", price * salerate)

# kim()
# salerate = 1.1
# lee()


# price = 1000
# def sale():
#     price = 500
# sale()
# print(price)
# price = 1000
# def sale():
#     price = 500
#     print("sale", id(price))


# sale()
# print("global", id(price))

# price = 1000
# def sale():
#     global price
#     price = 500

# sale()
# print(price)

# a = "python"

# for i in a:
#     print(i)


s = 'python'
# print(s[2])
# print(s[-2])
# s = 'python'
# for c in s:
#     print(c, end = ',')

# s = 'python'
# s[2] = 'k'

# s = 'python'
# print(s[2:5])
# print(s[3:])
# print(s[:4])
# print(s[2:-2])

# for i in range(0,len(s)):
#     print(s[i])


# file = '20220416-033630.ppt'
# print("찰영 날짜: " + file[4:6] + "월" + file[6:8] + '일')
# print("찰영 시간 : " + file[9:11] + '시'+ file[11:13] + "분")
# print("확장자 : " + file[-3:])

# yoil = '월화수목금토일'
# print(yoil[::2])
# print(yoil[::-1])

# s = "puthon programming"
# print(len(s))
# print(s.find('o'))
# print(s.rfind('o'))
# print(s.index('r'))
# print(s.count('n'))

# s = """생각이란 생각할수록 생각나므로 생각하지 말아야 할 생각은 생각하지 않으려고 하는 생각이 옳은 생각이라고 생각하고 또 생각하고 또또 생각한다."""
# print("생각 출연 횟수: ", s.count('생각'))

# s = "[python programming]"
# print('a' in s)
# print('z' in s)
# print('pro' in s)
# print('x' not in s)


# s = "good morning. my love KIMI"
# print(s.lower())
# print(s.upper())
# print(s)

# print(s.swapcase())
# print(s.capitalize())
# print(s.title())
