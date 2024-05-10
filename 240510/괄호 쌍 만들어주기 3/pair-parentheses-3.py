from sys import stdin
base = stdin.readline().strip()
n = len(base)

R = [0 for _ in range(n)]
cnt = 0
for i in range(n-1,-1,-1):
    if base[i] == ")":
        cnt += 1
    R[i] = cnt
# print(R)

ans = 0
for i in range(n):
    if base[i] == "(":
        ans += R[i]
print(ans)