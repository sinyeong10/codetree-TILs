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
max_value = float("-inf")
total = 0 #앞의 합산 값
for i in range(n):
    if total < 0: #-이면 포함하지 않는 게 이득, 따라서 지금부터 다시 시작!
        total = base[i]
    else: #아니면 현재값을 더함
        total += base[i]
    max_value = max(max_value, total)
    # print(i, total)
print(max_value)