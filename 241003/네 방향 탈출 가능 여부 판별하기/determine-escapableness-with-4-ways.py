from collections import deque

import sys
sys.setrecursionlimit(10**5)
from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited_2d = [[False for _ in range(m)] for _ in range(n)]

def can_go(x,y):
    if not(0<=x<n and 0<=y<n):
        return False
    elif visited_2d[x][y]:
        return False
    elif base_2d[x][y] == 0:
        return False
    else:
        return True

q = deque()

def bfs():
    dxs, dys = [-1,1,0,0], [0,0,-1,1]
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            next_x, next_y = cur_x+dx, cur_y+dy
            if can_go(next_x, next_y):
                q.append((next_x, next_y))
                visited_2d[next_x][next_y] = True


visited_2d[0][0] = True
q.append((0,0))
bfs()

print(1 if visited_2d[-1][-1] else 0)