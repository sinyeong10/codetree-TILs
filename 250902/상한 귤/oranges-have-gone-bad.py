from collections import deque

n, k = map(int, input().split())
step = [list(map(int, input().split())) for _ in range(n)]

q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and step[x][y] == -2 and not visited[x][y]

def push(new_x, new_y, new_step):
    q.append((new_x, new_y))
    visited[new_x][new_y] = True
    step[new_x][new_y] = new_step
    
for i in range(n):
    for j in range(n):
        if step[i][j] == 2:
            step[i][j] = 0
            push(i,j,0)
        elif step[i][j] == 0:
            step[i][j] = -1
        elif step[i][j] == 1:
            step[i][j] = -2

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

while q:
    x, y = q.popleft()    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            push(new_x, new_y, step[x][y] + 1)

for elem in step:
    print(*elem)
