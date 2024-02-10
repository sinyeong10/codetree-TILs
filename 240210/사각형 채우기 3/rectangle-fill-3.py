from sys import stdin
n = int(stdin.readline())

dp = [0 for _ in range(n+1)]

dp[0] = 1
dp[1] = 2

#마지막에 mod연산을 하는 것보다 진행하면서 하는 것이 연산 상에 오버플로우를 막을 수 있다!

for i in range(2, n+1):
    dp[i] = dp[i-1]*2 + dp[i-2]*3
    for j in range(2, i):
        dp[i] += dp[i-(j+1)]*2

print(dp[-1]%1000000007)