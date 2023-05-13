def calc(num1 , num2):
    c = input("원하는 부호 +,-,*,/ 를 입력해주세요 :")
    if c == '+':
        result = (num1) + (num2)
    elif c == '-':
        result = (num1) - (num2)
    elif c == '*':
        result = (num1) * (num2)
    elif c == '/':
        result = (num1) / (num2)
    else:
        print("올바른 부호를 써주세요")
        return 0
    
    print("해당 식은" , num1,c , num2 , '=', result, '입니다.')
                    
    
    return result


num1 = int(input("첫번째 값을 입력해주세요 :"))
num2 = int(input("두번째 값을 입력해주세요 :"))

test = calc(num1, num2)

