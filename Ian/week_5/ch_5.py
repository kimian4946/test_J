# def god(num1):
#     student = 1
#     b = int(input("입력하세여 ; "))
#     while student <= b:
#         print(num1)
#         student += 1
        
#     return num1

def make_star(num): 
    while True:
        i = int(input("줄 크기를 입력하세요:")) 
        for y in range(num,i):
            for x in range(y):
                print('*', end = "")
            print()
    return 0
test = make_star(1)



print





# test = god(6)



# print(god(1))

# student = 1
# while student <= 5:
#     print(student, '번 학생의 성적을 처리한다')
#     student += 1

# num = 1
# sum = 0

# while num <= 100:
#     sum += num
#     num += 1
# print("sum =", sum)

# num = 151
# sum = 0
# while num <= 300:
#     sum += num 
#     num += 2
# print("sum = ", sum )
# a = 5
# student = 1
# b = int(input("입력하세여 ; "))
# while student <= b:
#     print(a)
#     student += 1


# a = 5
# student = 1
# b = int(input("입력하세여 ; "))
# while student <= b:
#     print(a)
#     student += 1
