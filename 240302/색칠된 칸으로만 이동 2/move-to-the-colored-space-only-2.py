from sys import stdin
m, n = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(m)] #m*n 행이 m개
color_2d = [list(map(int, stdin.readline().split())) for _ in range(m)] #m*n 행이 m개
visited = [[False]*n for _ in range(m)] #m*n

def in_range(i,j):
    return 0<=i<m and 0<=j<n

from collections import deque
def bfs(i,j,D):
    # print(i, j, D)
    q = deque()
    visited[i][j] = True
    q.append((i,j))

    dx, dy = [-1,1,0,0], [0,0,-1,1]

    while q:
        x, y = q.popleft()
        # print(x,y)
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if in_range(next_x, next_y) and not visited[next_x][next_y] and abs(base_2d[x][y]-base_2d[next_x][next_y]) <= D:
                visited[next_x][next_y] = True
                q.append((next_x, next_y))

    for i in range(m):
        for j in range(n):
            if color_2d[i][j] == 1 and not visited[i][j]: #현재 위치가 색칠된 칸이고 방문을 안했으면 불가능!
                return False
    return True

def check(D):
    global visited
    visited = [[False]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if color_2d[i][j] == 1: #색깔인 경우만 한번 시도
                if bfs(i,j,D): #i,j에서 D차이로 이동하여 모든 색칠된 칸에서 가능!
                    return True
                else:
                    return False

left = 0
right = 10**9
min_value = 10**9
while left <= right:
    mid = (left+right)//2
    if check(mid):
        right = mid-1
        min_value = min(min_value, mid)
    else:
        left = mid+1
print(min_value)