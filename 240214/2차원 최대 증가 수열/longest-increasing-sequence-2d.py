from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp_2d = [[0]*n for _ in range(n)]
dp_2d[0][0] = 1

for i in range(1, n):
    for j in range(1, n):

        #이전 위치의 값을 가져옴
        if base_2d[i][j] <= base_2d[0][0]:
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
    for j in range(n):
        max_value = max(max_value, dp_2d[i][j])
print(max_value)