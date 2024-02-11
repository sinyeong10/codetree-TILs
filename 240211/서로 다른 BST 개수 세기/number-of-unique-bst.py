from sys import stdin
n = int(stdin.readline())

dp = [0 for _ in range(n+1)]

dp[0] = 1
dp[1] = 1
# dp[2] = 2
# dp[3] = 5

for i in range(2, n+1):
    for j in range(1, i+1): #루트가 j인 경우!
        dp[i] += dp[j-1] * dp[i-j] #좌측의 트리, 우측의 트리!
        # print(i,j,dp[i], dp[j-1], dp[i-j])
print(dp[-1])