from sys import stdin
n, k, u, d = list(map(int, stdin.readline().split())) #k개의 도시를 시작지로, u~d사이여야지 이동가능!
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
start_visited = [[False]*n for _ in range(n)]
def in_range(i,j):
    return 0<=i<n and 0<=j<n

from collections import deque
def bfs(start):
    visited = [[False]*n for _ in range(n)]
    q = deque()
    total = 0
    for i in range(k):
        x, y = start[i]
        q.append((x,y))
        visited[x][y] = True
        total += 1

    dx, dy = [-1,1,0,0], [0,0,-1,1]

    while q:
        x, y = q.popleft()
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if in_range(next_x, next_y) and not visited[next_x][next_y] and (u<=abs(base_2d[x][y]-base_2d[next_x][next_y])<=d):
                total += 1
                visited[next_x][next_y] = True
                q.append((next_x, next_y))
    return total

pick = []
def sol(cnt): #현재 cnt개를 고름
    max_value = 0
    if cnt == k:
        max_value = bfs(pick)
        # print(pick, max_value)
        return max_value

    for i in range(n):
        for j in range(n):
            if start_visited[i][j]:
                continue
            pick.append((i,j))
            start_visited[i][j] = True
            max_value = max(max_value, sol(cnt+1))
            pick.pop()
            start_visited[i][j] = False
    return max_value
print(sol(0))