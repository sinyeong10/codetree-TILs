from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
direct_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx, dy = [0,-1,-1,0,1,1,1,0,-1],[0,0,1,1,1,0,-1,-1,-1] #번째 단위로 1~8까지 방향
r,c = list(map(int,stdin.readline().split()))

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def sol(x,y):
    direct = direct_2d[x][y]
    value = base_2d[x][y]
    count = 0
    # print(x,y, direct, value)
    while in_range(x,y):
        next_dx, next_dy = x+dx[direct], y+dy[direct]
        if in_range(next_dx, next_dy) and base_2d[next_dx][next_dy] > value:
            count = max(count, sol(next_dx, next_dy)+1) #다음 위치에서 이동하는 경우에 현재 1이동하는 것
        x,y = next_dx, next_dy
    return count

print(sol(r-1,c-1)) #인덱스 단위로 전달