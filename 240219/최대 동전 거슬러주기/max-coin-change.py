from sys import stdin
n, m = list(map(int, stdin.readline().split()))
coin = list(map(int, stdin.readline().split()))

dp = [0]*(m+1)
for i in range(1, m+1):
    for j in coin:
        if i >= j:
            dp[i] = max(dp[i], dp[i-j]+1)
print(dp[-1])