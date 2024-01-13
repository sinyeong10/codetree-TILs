from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

visited = [[-1]*m for _ in range(n)]

from collections import deque
q = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<m and base[x][y] == 1

def bfs():
    dx, dy = [-1,1,0,0], [0,0,-1,1] #상하좌우

    while q:
        x, y = q.popleft()
        # print(x,y)

        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if in_range(next_x, next_y) and visited[next_x][next_y] == -1: #이동 가능, 방문x
                visited[next_x][next_y] = visited[x][y]+1 #방문 표시
                q.append([next_x, next_y]) #이동 목록에 넣음


#초기 시작 위치 설정
q.append([0,0])
visited[0][0] = 0

bfs()
print(visited[n-1][m-1])

# for elem in visited:
#     print(*elem)