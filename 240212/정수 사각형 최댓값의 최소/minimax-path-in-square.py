from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp_2d = [[0]*n for _ in range(n)]
dp_2d[0][0] = base_2d[0][0]
for j in range(1,n):
    dp_2d[0][j] = max(dp_2d[0][j-1], base_2d[0][j])
for i in range(1,n):
    dp_2d[i][0] = max(dp_2d[i-1][0], base_2d[i][0])

dx, dy = [0, -1], [-1, 0] #왼, 위

for i in range(1, n):
    for j in range(1, n):
        min_value = float("inf")
        for dxs, dys in zip(dx, dy):
            prev_i, prev_j = i+dxs, j+dys
            min_value = min(min_value, dp_2d[prev_i][prev_j])
        dp_2d[i][j] = max(min_value, base_2d[i][j])
print(dp_2d[-1][-1])