from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
visit_2d = [[False for _ in range(n)] for _ in range(n)]
start = [list(map(int, stdin.readline().split())) for _ in range(k)]

def can_go(x,y):
    if not(0<=x<n and 0<=y<n):
        return False
    elif base_2d[x][y] == 1:
        return False
    elif visit_2d[x][y]:
        return False
    else:
        return True

from collections import deque
q = deque()
for x, y in start:
    visit_2d[x-1][y-1] = True
    q.append((x-1,y-1))
    # print(x-1,y-1)
cnt = k
def bfs():
    global cnt
    dxs, dys = [-1,1,0,0],[0,0,-1,1]
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            next_x, next_y = cur_x+dx, cur_y+dy
            if can_go(next_x, next_y):
                # print(next_x, next_y)
                visit_2d[next_x][next_y] = True
                cnt += 1
                q.append((next_x, next_y))
bfs()
print(cnt)

# for elem in visit_2d:
#     print(*elem)