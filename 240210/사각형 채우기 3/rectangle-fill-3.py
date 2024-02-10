from sys import stdin
n = int(stdin.readline())

dp = [0 for _ in range(n+1)]

dp[0] = 1
dp[1] = 2

for i in range(2, n+1):
    dp[i] = dp[i-1]*2 + dp[i-2]*3
    if i > 2:
        dp[i] += dp[i-3]*2

print(dp[-1]%1000000007)