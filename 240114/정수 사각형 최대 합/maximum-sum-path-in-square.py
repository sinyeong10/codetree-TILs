from sys import stdin
n = int(stdin.readline())
base = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

#초기값
dp[0][0] = base[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0]+base[i][0]

for j in range(1, n):
    dp[0][j] = dp[0][j-1]+base[0][j]

#테두리를 채웠기에 범위 밖인지 체크없이 처리
dx, dy = [0, -1], [-1, 0] #좌, 상
for i in range(1, n):
    for j in range(1, n):
        max_value = 0
        for dxs, dys in zip(dx, dy):
            max_value = max(max_value, dp[i+dxs][j+dys])
        dp[i][j] = max_value+base[i][j] #가장 큰 이전 상태에서 현재 가산되는 값을 더해서 처리

# for elem in dp:
#     print(*elem)

print(dp[n-1][n-1])