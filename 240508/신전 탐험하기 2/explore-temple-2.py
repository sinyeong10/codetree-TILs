from sys import stdin
n = int(stdin.readline())
base = []
for _ in range(n):
    base.append(list(map(int, stdin.readline().split())))

dp = [[0]*3 for _  in range(n)]

for start in range(3):
    dp[0] = base[0][:]
    dp[0][start] = 0
    # print(dp[0], base[0])
    for i in range(1, n-1):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp[i][j] = max(dp[i][j], base[i][j]+dp[i-1][k])
    for k in range(3):
        if start == k:
            continue
        dp[-1][start] = max(dp[-1][start], base[-1][start]+dp[-2][k])
print(max(dp[-1]))


# dp[-1] = base[-1]

# if n > 1:
#     dp[1] = base[1]

# for i in range(2, n-1): #처음과 마지막은 제외
#     for j in range(3):
#         for k in range(3):
#             if j == k:
#                 continue
#             dp[i][j] = max(dp[i][j], dp[i-1][k]+base[i][j])
# print(dp)