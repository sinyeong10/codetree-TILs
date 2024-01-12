from sys import stdin
from collections import deque
n,m = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

q = deque()

def can_go(x,y):
    if not (0<=x<n and 0<=y<m): #범위 체크
        return False
    if base[x][y] == 0 or visited[x][y]: #갈 수 있는지, 방문했는지 체크
        return False
    return True

def bfs():
    dx, dy = [-1,1,0,0], [0,0,-1,1] #상하좌우

    while q:
        x, y = q.popleft() #deque에서 left를 붙일 시 처음 의미!
        visited[x][y] = True
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if can_go(next_x, next_y):
                q.append([next_x, next_y])

q.append([0,0])
bfs()

# for elem in visited:
#     print(*elem)
print(1 if visited[n-1][m-1] else 0)