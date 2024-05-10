from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

#완전탐색
# cnt = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if base[i] <= base[j] <= base[k]:
#                 cnt += 1
# print(cnt)

L = [0 for _ in range(n)]
for i in range(n):
    tmp = 0
    for j in range(i):
        if base[j] < base[i]:
            tmp += 1
    L[i] = tmp
# print(L)


R = [0 for _ in range(n)]
for i in range(n-1,-1,-1):
    tmp = 0
    for j in range(i+1, n):
        if base[j] > base[i]:
            tmp += 1
    R[i] = tmp
# print(R)


cnt = 0
for i in range(n):
    cnt += L[i] * R[i]
print(cnt)