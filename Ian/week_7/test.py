word = "korea"


# for i in word:
#     print(i)
#print(word[1])
#word[1] == "o"

# a = 'abc'
# b = 'def'
# c = a+b
# print(c)
# a = ''

# korea -> kzrea

find_num = word.find('o')
# print(find_num)
result_word = ''

for i in range(len(word)):
    if i == find_num:
        result_word += 'z'
    else:
        result_word += word[i]


print(result_word)