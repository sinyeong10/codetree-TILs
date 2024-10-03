from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _  in range(n)]
visit_2d = [[False for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y):
    global cnt
    dxs, dys = [1,-1,0,0], [0,0,-1,1]

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x+dx, y+dy
        if in_range(next_x, next_y) and not visit_2d[next_x][next_y] and base_2d[next_x][next_y] == 1:
            visit_2d[next_x][next_y] = True
            cnt += 1
            dfs(next_x, next_y)

city = []

for i in range(n):
    for j in range(n):
        if not visit_2d[i][j] and base_2d[i][j] == 1:
            cnt = 1
            visit_2d[i][j] = True
            dfs(i,j)
            city.append(cnt)

# print(city)
city.sort()
print(len(city))
for elem in city:
    print(elem)