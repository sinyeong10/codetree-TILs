from sys import stdin
n = int(stdin.readline())
base = [list(map(int, stdin.readline().split())) for _ in range(2*n)]

dp = [[0]*(n+1) for _ in range(2*n+1)] #i는 현재까지 본 갯수, j는 첫번째 선택의 갯수


for i in range(1, 2*n+1):
    dp[i][0] = dp[i-1][0]+base[i-1][1]

# for elem in dp:
#     print(*elem)

for i in range(1, n+1):
    dp[i][i] = dp[i-1][i-1]+base[i-1][0]

# for elem in dp:
#     print(*elem)
# print()

for i in range(2, 2*n+1):
    for j in range(1, n+1):
        # print(base[i-1])
        dp[i][j] = max(dp[i-1][j]+base[i-1][1], dp[i-1][j-1]+base[i-1][0])

# for elem in dp:
#     print(*elem)

print(dp[2*n][n])