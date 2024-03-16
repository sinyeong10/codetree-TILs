from sys import stdin
word = stdin.readline().strip()

count = {}
for elem in word:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

flag = True
#딕셔너리가 입력 순서대로 저장되는 것이 보장될 시
for key, value in count.items():
    if flag and value == 1:
        flag = False
        print(key)

# #word로 순회해도 됨!
# for elem in word:
#     if flag and count[elem] == 1:
#         flag = False
#         print(elem)


if flag: #앞에서 출력이 안됨!
    print("None")