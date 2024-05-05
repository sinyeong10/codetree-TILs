from sys import stdin
n = int(stdin.readline())

dp = [[0]*10 for _ in range(n)]

for j in range(1, 10):
    dp[0][j] = 1
# print(dp)

divide_value = 10**9+7

for i in range(1, n):
    for j in range(10):
        if j != 0 and dp[i-1][j-1] > 0: #이전에 가능했다면
            dp[i][j] += dp[i-1][j-1]
        if j != 9 and dp[i-1][j+1] > 0:
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= divide_value
# for elem in dp:
#     print(elem)
print(sum(dp[-1])%divide_value)