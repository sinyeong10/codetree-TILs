from sys import stdin
n = int(stdin.readline())

dp = [0 for _ in range(n+1)]

dp[1] = 1

#2번째 값을 설정하지 않을 수 있음!
if n > 1:
    dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])