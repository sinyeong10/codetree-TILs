from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
step_2d = [[-1 for _  in range(m)] for _  in range(n)]

from collections import deque
q = deque()
step_2d[0][0] = 0
q.append((0,0))

def can_go(x,y):
    if not(0<=x<n and 0<=y<m):
        return False
    elif base_2d[x][y] == 0:
        return False
    elif step_2d[x][y] != -1:
        return False
    else:
        return True

def bfs():
    dxs, dys = [-1,1,0,0],[0,0,-1,1]
    while q:
        cur_x, cur_y = q.popleft()
        step = step_2d[cur_x][cur_y]
        for dx, dy in zip(dxs, dys):
            next_x, next_y = cur_x+dx, cur_y+dy
            if can_go(next_x, next_y):
                step_2d[next_x][next_y] = step+1
                q.append((next_x, next_y))

bfs()
print(step_2d[-1][-1])