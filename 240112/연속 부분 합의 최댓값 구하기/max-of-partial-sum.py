from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

dp = [float("-inf") for _ in range(n)] #-float("inf")는 float("-inf")
# print(dp)

dp[0] = base[0]

for i in range(1, n):
    dp[i] = max(base[i], dp[i-1]+base[i])

# print(dp)
print(max(dp))