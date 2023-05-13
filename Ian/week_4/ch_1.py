

#n = int(input("끝의 값을 입력하시오 : "))

#for i in range(0, n):
#
#    if i%10 == 3 or i%10 == 6 or i%10 == 9: print("짝", end=" ")
#
##    else: print(i, end=" ")

#s = int(input("끝 값을 입력해주세요 : "))
#b = int(input("박수를 칠 첫번째 숫자를 입력하세요 :"))
#c = int(input("박수를 칠 두번째 숫자를 입력하세요 :"))
#d = int(input("박수를 칠 세번째 숫자를 입력하세요 :"))
#for m in range(0, s):

#    if m%10 == b or m%10 == c or m%10 == d: 
#        print("짝", end=" ")
   # 
#    else: print(m, end=" ")

#s = int(input("시간을 입력하시오"))
#for i in range(1, s):
#    if (i <= 0 or i >= 24):
#        print("값을 잘못 입력하셨습니다.")
#        break
#    else:
#        print(i)
 #       continue

# for dan in range(2, 10):
#     print(dan, '단')
#     for hang in range(2, 10):
#         print(dan, "*", hang, "=", dan * hang)
#     print()
    

# dan = 2
# while dan <= 9:
#     hang = 2
#     print(dan, "단")
#     while hang <= 9:
#         print(dan, "*", hang, "=", dan * hang)
#         hang += 1
#     dan += 1
#     print()

# s = int(input("원하는 단 입력 : "))
# n = 0
# if s == s:
#     for dan in range(s, 10):
#         print(dan, "단")
#         for hang in range(1, 10):
#             print(dan, "x", hang, '=',  dan * hang)
#         print()
# s = 0
# l = 0
# while s <= 10:
#     while l <= 5:
#         print("*")
#         l -= 1
#     s += 1

# for y in range(1, 10):
#     for z in range(10,y,-1):
#         print(' ',end='')
#     for x in range(y):
#         print('*', end = '')
#     print()



# print("3 ** 4 = ?")
# while True:
#     a = int(input("정답을 입력하시오"))
#     if (a == 81):
#         break
# print('참 잘 했 어 요 ,')


# for ten in range(0, 5)                                                                                                                                                      :
#     for num in range(ten * 10, ten * 10 +10)                                                                                                                               :
#         print(num, end = ',')
#     print()

# for n in range(1, 10):
#     print(' ' * (10-n) + '*'*(1*n-1))



# for n in range(1, 10):
#     print(' ' * (10-n) + '*'*(2*n-1))

# def function(a,b):
#     for i in range(a,b):
#         print(i)
#     return 0

# function(1,5)

def ch1_sum():
    sum = 0
    for num in range( 5):
        sum += num
    print("~ 4 = ", sum)

    sum = 0
    for sum in range(11):
        sum + num
    print("~10 =", sum)

def calcum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

# ch1_sum()




print("~ 4 = ", calcum(4))
# print("~ 10 =", calcum(10))


