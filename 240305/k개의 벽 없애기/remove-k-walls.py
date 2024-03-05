from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
r1, c1 = list(map(int, stdin.readline().split()))
r2, c2 = list(map(int, stdin.readline().split()))

def in_range(i,j):
    return 0<=i<n and 0<=j<n


import sys
from collections import deque
def bfs(i,j):
    q = deque()
    visited = [[sys.maxsize]*n for _ in range(n)] #여러 경로중 최소를 선택해야하므로 sys.maxsize로 초기화!
    #이것만으로 가면서 벽을 없애면서 처리하지 못함.. 돌아가면서 더 적게 없애야 할 경우 판별이 힘듦..
    # remove_count = [[0]*n for _ in range(n)]
    q.append((i,j))
    visited[i][j] = 0
    
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    while q:
        x, y = q.popleft()
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if in_range(next_x, next_y) and visited[next_x][next_y] == sys.maxsize: #범위 안이고 아직 방문 안함
                if base_2d[next_x][next_y] == 0: #이동가능
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = visited[x][y] + 1
                    # remove_count[next_x][next_y] = remove_count[x][y]
                # else: #돌이 있음
                #     if remove_count[x][y] < k:
                #         q.append((next_x, next_y))
                #         visited[next_x][next_y] = visited[x][y] + 1
                #         remove_count[next_x][next_y] = remove_count[x][y]+1
        # print(x,y)
        # for elem in remove_count:
        #     print(*elem)
        # for elem in visited:
        #     print(*elem)
    return visited[r2-1][c2-1]

# print(bfs(r1-1,c1-1))

point = []
for i in range(n):
    for j in range(n):
        if base_2d[i][j] == 1:
            point.append((i,j))

pick = []
def sol(idx, cnt): #현재 idx를 보는 중이며 cnt개 고름!
    min_value = sys.maxsize
    if cnt == k:
        for i in range(k):
            x, y = point[pick[i]]
            base_2d[x][y] = 0

        min_value = min(min_value, bfs(r1-1, c1-1))
        
        for i in range(k):
            x, y = point[pick[i]]
            base_2d[x][y] = 1

        # print(pick, cnt, min_value)
        return min_value
    
    if idx == len(point):
        return min_value

    min_value = min(min_value, sol(idx+1, cnt))
    pick.append(idx)
    min_value = min(min_value, sol(idx+1, cnt+1))
    pick.pop()
    return min_value

ans = sol(0,0)
print(ans if ans != sys.maxsize else -1)