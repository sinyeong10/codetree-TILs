from sys import stdin
n = int(stdin.readline())
r1, c1, r2, c2 = list(map(int, stdin.readline().split()))

base_2d = [[-1 for _  in range(n)]for _ in range(n)]

def can_go(x,y):
    if not(0<=x<n and 0<=y<n):
        return False
    elif base_2d[x][y] != -1:
        return False
    else:
        return True

from collections import deque
q = deque()
base_2d[r1-1][c1-1] = 0
q.append((r1-1,c1-1))

def bfs():
    dxs, dys = [1,2,2,1,-1,-2,-2,-1],[-2,-1,1,2,2,1,-1,-2]
    while q:
        x,y = q.popleft()
        if x==r2-1 and y==c2-1:
            return
        step = base_2d[x][y]
        for dx, dy in zip(dxs, dys):
            next_x, next_y = x+dx, y+dy
            if can_go(next_x, next_y):
                base_2d[next_x][next_y] = step+1
                q.append((next_x, next_y))
bfs()
print(base_2d[r2-1][c2-1])