from sys import stdin
n = int(stdin.readline())
base = stdin.readline().strip()
target = stdin.readline().strip()

check = False #이 구간이 체크되어있는지!
total = 0
for i in range(n):
    if base[i] != target[i]: #다르면 해당 구간을 넣을지 고민
        if not check:
            check = True
            total += 1
    else: #같으면 체크되어있음
        check = False

print(total)

# #바꿔야할 위치
# trans = [0 for _ in range(n)]
# for i in range(n):
#     if base[i] != target[i]:
#         trans[i] += 1
# # print(trans)

# #연속된 1로 이뤄진 서로 다른 그룹의 수!
# total = 0
# idx = 0
# for i in range(n):
#     if trans[i] == 1 and trans[i] != idx: #처음 1일 때 갯수 증가!
#         total += 1
#     idx = trans[i]
# print(total)