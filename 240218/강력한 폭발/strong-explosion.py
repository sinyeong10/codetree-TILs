from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
bomb_dx = {1:(-1,-2,1,2),2:(-1,1,0,0),3:(-1,-1,1,1)}
bomb_dy = {1:(0,0,0,0),2:(0,0,-1,1),3:(-1,1,-1,1)}

bomb = []
for i in range(n):
    for j in range(n):
        if base_2d[i][j] == 1:
            bomb.append((i,j))

def in_range(x,y):
    if not (0<=x<n and 0<=y<n):
        return False
    if base_2d[x][y] != 0: #터질 위치가 아닌 경우! [이미 터짐 혹은 폭탄 위치]
        return False
    return True

def count():
    total = 0
    for i in range(n):
        for j in range(n):
            if base_2d[i][j] != 0:
                total += 1
    return total

bomb_type = []
def check(num):
    if num == len(bomb):
        # print(bomb_type, count())
        # for elem in base_2d:
        #     print(*elem)
        return count()
    max_value = 0
    x, y = bomb[num]
    for i in range(1,4):
        tmp = []
        bomb_type.append(i)
        for dxs, dys in zip(bomb_dx[i], bomb_dy[i]):
            next_x, next_y = x+dxs, y+dys
            if in_range(next_x, next_y):
                # print(next_x, next_y, base_2d[next_x][next_y])
                tmp.append((next_x, next_y))
                base_2d[next_x][next_y] = 2
        max_value = max(max_value, check(num+1))
        bomb_type.pop()
        for tmp_x, tmp_y in tmp:
            base_2d[tmp_x][tmp_y] = 0
        # print(bomb_type)
        # for elem in base_2d:
        #     print(*elem)
    return max_value

print(check(0))