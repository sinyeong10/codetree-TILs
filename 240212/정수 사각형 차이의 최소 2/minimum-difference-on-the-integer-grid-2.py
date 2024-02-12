from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp_2d = [[(100, 1)]*n for _ in range(n)] #최소 최대로 갱신!

min_value, max_value = min(base_2d[0][0], base_2d[-1][-1]), max(base_2d[0][0], base_2d[-1][-1])
dp_2d[0][0] = (min_value, max_value)
for j in range(1,n):
    min_value, max_value = dp_2d[0][j-1]
    min_value = min(min_value, base_2d[0][j])
    max_value = max(max_value, base_2d[0][j])
    dp_2d[0][j] = (min_value, max_value)

for i in range(1, n):
    min_value, max_value = dp_2d[i-1][0]
    min_value = min(min_value, base_2d[i][0])
    max_value = max(max_value, base_2d[i][0])
    dp_2d[i][0] = (min_value, max_value)

dx, dy = [0,-1],[-1,0] #왼쪽, 위 체크

for i in range(1, n):
    for j in range(1, n):
        standard = float("inf")
        for dxs, dys in zip(dx, dy):
            prev_i, prev_j = i+dxs, j+dys
            min_value, max_value = dp_2d[prev_i][prev_j]
            if standard > max_value-min_value: #차이가 더 작으면 갱신
                standard = max_value - min_value #이걸로 기준이 바껴서 이전보다 작을 시 반영
                min_value = min(min_value, base_2d[i][j])
                max_value = max(max_value, base_2d[i][j])
                dp_2d[i][j] = min_value, max_value

        # print(i,j)
# for elem in dp_2d:
#     print(*elem)

a,b = dp_2d[-1][-1]
print(b-a)