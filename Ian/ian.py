# 구구단
# n = n단
# a=int(input(''))
# for n in range (1,10):
#     b = a * n
#     print(a ,'*', n , '=', b)


# 구구단 전체 출력 #1: 8 end

# print("구구단")
# for n in range (1, 10): #곱해지는 수
#     for sum in range(2,10): #단
#         print(sum,'x', n,'=', n*sum  ,end = '\t')
#     print()
            


# for n in range(2,10): #구구단의 단
#     for sum in range(1,10): #곱해지는 수
#         print(n,"*", sum,"=",n*sum)


# a + b
# t = 계산 회수

# a = int(input('>')) 

# for sum in range(a):
#     b,c = input('>').split
#     print(int(c)+int(b))

# t = int(input("계산 회수: "))

# for i in range(t):
#     a= int(input(">>"))
#     b= int(input(">>"))
#     c=(a) + (b)
#     print(c)


# 합

# a=int(input(">"))  #5
# b=0

# for sum in range(1,a+1):   #1~5 sum  1,2,3,4,5
#     b = b + sum    
    
# print(b)


# 영수증
# x = 총 금액
# n = 물건 종류의 수
# a = 물건의 가격
# b = 물건의 개수

e = 0
a=int(input(">")) #영수증의 총 금액
b=int(input(">>")) #물건의 개수

for sum in range(b):
    c=int(input(">>>")) #물건의 가격
    d=int(input(">>>>")) #c물건의 개수
    e += c * d
    # 20000 * 5  100000
    # 30000 * 2  60000
    # 10000 * 6  60000
    # 5000 * 8  40000
if e == a:
    print("yes")
elif e > a:
    print("no")
elif e < a:
    print("no")


# x = int(input("영수증의 총 금액: "))
# n = int(input("물건 종류의 수: "))
# total = 0

# for i in range(n):
#     a = int(input("물건 가격: "))
#     b = int(input("물건 개수: "))

#     total += a*b

# if x == total:
#     print("YES")
# else:
#     print("NO")













































