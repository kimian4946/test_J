def calc(num1, num2):
    if e == '+':
        result = (num1) + (num2)
    elif e == '-':
         result = (num1) - (num2)
    elif e == '*':
         result = (num1) * (num2)
    elif e == '**':
         result = (num1) ** (num2)
    elif e == '//':
         result = (num1) // (num2)
    elif e == '/':
         result = (num1) / (num2)
    elif e == '&':
         result = (num1) & (num2)


    print(num1, e , num2, '=' ,result)
    
    return result



num = 10
s = str(input("원하는 숫자를 입력하세요"))
if s == '1':
    while num > 0:
         print(num)
         num -= 1
    if num == 0:
         print("미사일 발사")
if s == '2':
    b = int(input("별의 개수를 입력하시오"))
    for y in range(b , 0  , -1 ):
        for x in range(y):
            print('*', end = '')
        print()
if s == '3':
    num1 = int(input("첫번째 값 입력하세요"))
    num2 = int(input("두번째 값 입력하세요"))
    e = str(input("부등호 선택 +, - , * , ** , // , / , &"))
    test = calc(num1, num2)
    





