from sys import stdin
n = int(stdin.readline())

import sys
dp = [sys.maxsize for _ in range(n+1)]
if n >= 2:
    dp[2] = 1
if n >= 5:
    dp[5] = 1
for i in range(n+1):
    if dp[i] > 0: #가능한 경우만!
        if i+2 <= n:
            dp[i+2] = min(dp[i+2], dp[i]+1)
        if i+5 <= n:
            dp[i+5] = min(dp[i+5], dp[i]+1)
# print(dp)
print(dp[n] if dp[n]!=sys.maxsize else -1)