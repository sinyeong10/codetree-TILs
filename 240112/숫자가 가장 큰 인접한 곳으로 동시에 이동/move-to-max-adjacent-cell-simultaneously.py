from sys import stdin
n, m, t = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]
ball = [list(map(int, stdin.readline().split())) for _ in range(m)]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def move():
    global ball
    tmp = [[0]*n for _ in range(n)]
    next_ball = []

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #상하좌우

    for i in range(len(ball)):
        x, y = ball[i]
        next_pos = [-1, -1]
        value_max = 0
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x-1+dxs, y-1+dys
            if in_range(next_x, next_y) and base[next_x][next_y] > value_max:
                value_max = base[next_x][next_y]
                next_pos = [next_x, next_y]
        tmp[next_pos[0]][next_pos[1]] += 1
    
    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 1:
                next_ball.append([i, j])
    ball = next_ball

for _ in range(t):
    move()
print(len(ball))