from sys import stdin
n, m = list(map(int, stdin.readline().split()))
coin = list(map(int, stdin.readline().split()))

dp = [-1]*(m+1)
dp[0] = 0
for i in range(1, m+1):
    for j in coin:
        if i >= j and dp[i-j] != -1: #불가능한 경우를 제외
            dp[i] = max(dp[i], dp[i-j]+1)
print(dp[-1])