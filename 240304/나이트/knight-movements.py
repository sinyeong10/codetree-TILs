from sys import stdin
n = int(stdin.readline())
r1, c1, r2, c2 = list(map(int, stdin.readline().split()))

def in_range(i,j):
    return 0<=i<n and 0<=j<n

from collections import deque
def dfs(i,j):
    visited = [[-1]*n for _ in range(n)] #불가능시 -1이라서 -1
    q = deque()
    q.append((i,j))
    visited[i][j] = 0

    dx, dy = [-1,-2,-2,-1,1,2,2,1],[-2,-1,1,2,-2,-1,1,2]

    while q:
        x, y = q.popleft()
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if in_range(next_x, next_y) and visited[next_x][next_y] == -1: #이미 갔으면 더 많은 횟수로 돌아가는 것이므로 아직 안간 곳만 감!
                visited[next_x][next_y] = visited[x][y]+1
                q.append((next_x, next_y))
    return visited[r2-1][c2-1]

print(dfs(r1-1,c1-1))