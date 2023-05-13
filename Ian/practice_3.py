# nm =11
# while nm > 0:
#     nm -= 1
#     print(nm)

# print("미사일 발사")

p = int(input("나이 입력 : "))
t = 0
while True:
    if p < 20:
        print("미성년자는 22시 이후에 접속이 불가능합니다.")
        p = int(input("나이 입력 : "))
    if p > 20:
        print("성인 입장 가능")
        p = int(input("나이 입력 : "))

# for y in range(1, 10 - 1):
#     for x in range(y):
#         print('쿵짝 쿵짝', end = '')
#     print()  