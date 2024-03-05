from sys import stdin
n = int(stdin.readline())
coin = list(map(int, stdin.readline().split()))
dp = [[-1]*4 for _ in range(n+1)] #i는 현재까지 올라간 계단, j는 1계단 올라간 횟수!

dp[0][0] = 0
dp[1][1] = coin[0]

for i in range(2,n+1):
    if dp[i-2][0] != -1:
        dp[i][0] = dp[i-2][0]+coin[i-1]
    for j in range(1, 4):
        dp[i][j] = max(dp[i-1][j-1], dp[i-2][j])
        if dp[i][j] != -1:
            dp[i][j] += coin[i-1]

# for elem in dp:
#     print(*elem)
print(max(dp[-1]))