from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _  in range(n)]

dp_2d = [[0 for _ in range(n)] for _ in range(n)]
dp_2d[0][0] = base_2d[0][0]

for j in range(1, n):
    dp_2d[0][j] = dp_2d[0][j-1]+base_2d[0][j]

for i in range(1, n):
    dp_2d[i][0] = dp_2d[i-1][0]+base_2d[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp_2d[i][j] = max(dp_2d[i-1][j], dp_2d[i][j-1]) + base_2d[i][j]

# for elem in dp_2d:
#     print(*elem)

print(dp_2d[-1][-1])