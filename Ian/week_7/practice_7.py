def find_word(num_find):
    #1번을 입력했을 경우 find_word 실행
    a = (word.find(num_find))
    
    return a


def replace_word():
    s = input("변경 단어를 입력")
    f = input("무슨 단어 변경?")
    find_num = word.find(s)

    result_word = ''

    for i in range(len(word)):
        if i == find_num:
            result_word += f
        else:
            result_word += word[i]


    print(result_word)
    return result_word

while True:
    word = input("string을 입력해주세요 : ")

    num = int(input("원하는 방법을 선택해주세요 (1:알파벳 찾기, 2:단어 변경하기)"))
    if num == 1:
        num_find = input("찾고자 하는 알파벳 입력")
        
        test55 = find_word(num_find)
        print(test55, "번째 위치에 찾고자 하는 알파벳" ,num_find, "이 있습니다.")
    elif num == 2:
        um = replace_word()
    else:
        print('1,2 중에 값을 입력해주세요')

    #computer 
    #1번 클릭 -> n번째 위치에 찾고자 하는 알파벳 ~ 이 있습니다.
    #2번 클릭 -> 수정된 알파벳은 다음과 같습니다. ~~~~ 

