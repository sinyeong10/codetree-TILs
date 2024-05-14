from sys import stdin
n = int(stdin.readline())
base = stdin.readline().strip()

L = [0 for _ in range(n)]
cnt = 0
for i in range(n):
    if base[i] == "C":
        cnt += 1
    L[i] = cnt

R = [0 for _ in range(n)]
cnt = 0
for j in range(n-1,-1,-1):
    if base[j] == "W":
        cnt += 1
    R[j] = cnt

# print(L,R)

ans = 0
for i in range(n):
    if base[i] == "O":
        ans += L[i]*R[i]
print(ans)