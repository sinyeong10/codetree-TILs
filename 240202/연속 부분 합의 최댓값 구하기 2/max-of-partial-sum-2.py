from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

# #dp 방식
# dp = [float("-inf") for _ in range(n)]
# dp[0] = base[0]
# for i in range(1, n):
#     dp[i] = max(dp[i-1]+base[i], base[i])
#     # print(dp)
# print(max(dp))

# 그리디 방식
max_value = 0
total = base[0]
for i in range(1, n):
    if total < 0:
        total = base[i]
    else:
        total += base[i]
    max_value = max(max_value, total)
print(max_value)