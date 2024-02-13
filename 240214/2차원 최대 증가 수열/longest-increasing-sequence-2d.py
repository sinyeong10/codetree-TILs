from sys import stdin
n, m = list(map(int, stdin.readline().split())) #nxn이 아니라 nxm이다 범위 잘 보자....
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp_2d = [[0]*m for _ in range(n)]
dp_2d[0][0] = 1

for i in range(1, n):
    for j in range(1, m):

        #이전 위치의 값을 가져옴
        if base_2d[i][j] <= base_2d[0][0]:
            # print(i,j)
            continue
        else:
            dp_2d[i][j] = 2

        for q in range(1, i):
            for w in range(1, j):
                if base_2d[i][j] > base_2d[q][w]:
                    dp_2d[i][j] = max(dp_2d[i][j], dp_2d[q][w]+1)

# print(dp_2d)

max_value = 0
for i in range(n):
    for j in range(m):
        max_value = max(max_value, dp_2d[i][j])
print(max_value)