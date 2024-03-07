from sys import stdin
n, h, m = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

from collections import deque
def bfs():
    visited = [[-1]*n for _ in range(n)]
    q = deque() #최종 도착위치로 부터 역순으로 감!
    for i in range(n):
        for j in range(n):
            if base_2d[i][j] == 3:
                q.append((i,j))
                visited[i][j] = 0
    dx, dy = [-1,1,0,0], [0,0,-1,1]

    while q:
        x,y = q.popleft()
        # print(x,y)
        for dxs, dys in zip(dx,dy):
            next_x, next_y = x+dxs, y+dys
            #범위 안, 아직 가지 않음, 벽이 아님
            if in_range(next_x, next_y) and visited[next_x][next_y] == -1 and base_2d[next_x][next_y] != 1:
                visited[next_x][next_y] = visited[x][y]+1
                q.append((next_x, next_y))
    
    # print(visited)

    ans = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if base_2d[i][j] == 2:
                ans[i][j] = visited[i][j]
    return ans

for elem in bfs():
    print(*elem)