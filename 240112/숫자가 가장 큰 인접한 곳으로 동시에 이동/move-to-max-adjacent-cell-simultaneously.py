from sys import stdin
n, m, t = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]
ball = [list(map(int, stdin.readline().split())) for _ in range(m)]

for i in range(m): #인덱스 변환 필요
    ball[i] = [ball[i][0]-1, ball[i][1]-1]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def move():
    global ball
    tmp = [[0]*n for _ in range(n)]
    next_ball = [] #아래에서 얉은 복사했지만 재할당하여 같은 객체 참조하지 않음!

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #상하좌우

    for i in range(len(ball)):
        x, y = ball[i]
        next_pos = [-1, -1]
        value_max = 0
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if in_range(next_x, next_y) and base[next_x][next_y] > value_max:
                value_max = base[next_x][next_y]
                next_pos = [next_x, next_y]
        tmp[next_pos[0]][next_pos[1]] += 1
    
    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 1:
                next_ball.append([i, j])
    ball = next_ball #수정이 일어나 전역변수 설정 필요!

for _ in range(t):
    move()
    # print(ball)
print(len(ball))