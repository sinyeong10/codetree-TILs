from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]
remove_count = [[0]*n for _ in range(n)]
r1, c1 = list(map(int, stdin.readline().split()))
r2, c2 = list(map(int, stdin.readline().split()))

def in_range(i,j):
    return 0<=i<n and 0<=j<n

from collections import deque
def bfs(i,j):

    q = deque()
    q.append((i,j))
    visited[i][j] = 0

    dx, dy = [-1,1,0,0], [0,0,-1,1]
    while q:
        x, y = q.popleft()
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if in_range(next_x, next_y) and visited[next_x][next_y] == -1: #범위 안이고 아직 방문 안함
                if base_2d[next_x][next_y] == 0: #이동가능
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = visited[x][y] + 1
                    remove_count[next_x][next_y] = remove_count[x][y]
                else: #돌이 있음
                    if remove_count[x][y] < k:
                        q.append((next_x, next_y))
                        visited[next_x][next_y] = visited[x][y] + 1
                        remove_count[next_x][next_y] = remove_count[x][y]+1
        # print(x,y)
        # for elem in remove_count:
        #     print(*elem)
        # for elem in visited:
        #     print(*elem)
    return visited[r2-1][c2-1]

print(bfs(r1-1,c1-1))