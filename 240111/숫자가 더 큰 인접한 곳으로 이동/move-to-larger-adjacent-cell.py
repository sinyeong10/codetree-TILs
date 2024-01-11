from sys import stdin
n, r, c = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

def in_range(i, j):
    if 0<=i<n and 0<=j<n:
        return True
    return False

def move():
    global x, y
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(base[x][y], end= " ")

    for dxs, dys in zip(dx, dy):
        next_x, next_y = x+dxs, y+dys
        if in_range(next_x, next_y) and base[next_x][next_y] > base[x][y]:
            x, y = next_x, next_y
            return True
    return False

x, y = r-1, c-1
while move():
    pass