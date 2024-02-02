from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
dp = [float("-inf") for _ in range(n)]
dp[0] = base[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+base[i], base[i])
    # print(dp)
print(max(dp))