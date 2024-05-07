from sys import stdin
n = int(stdin.readline())
base = []
for i in range(n):
    l, m, r = list(map(int, stdin.readline().split()))
    base.append([l, m, r])
# print(base)

dp = [[0]*3 for _ in range(n)]
dp[0] = base[0]

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][k]+base[i][j])
print(max(dp[-1]))