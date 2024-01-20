from sys import stdin
n = int(stdin.readline())
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bomb(x, y):
    num = base[x][y]

    dx, dy = [-1, 1,0,0], [0,0,-1,1]#상하좌우

    for i in range(num):
        if i == 0:
            tmp[x][y] = 0
            continue
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs*i, y+dys*i
            if in_range(next_x, next_y):
                tmp[next_x][next_y] = 0

def clear():
    for j in range(n):
        weight = 0
        for i in range(n-1, -1, -1):
            if tmp[i][j] == 0:
                weight += 1
            else:
                tmp[i+weight][j] = base[i][j]
            

def check():
    count = 0
    for i in range(n):
        for j in range(n):
            if tmp[i][j] == 0:
                continue
            if in_range(i, j+1) and tmp[i][j]==tmp[i][j+1]:
                count += 1
            if in_range(i+1, j) and tmp[i][j]==tmp[i+1][j]:
                count+=1 
    return count


max_value = 0
for i in range(n):
    for j in range(n): #터지는 위치
        tmp = [[0]*n for _ in range(n)]
        bomb(i, j) #i,j에서 폭발
        clear() #중력으로 아래로 떨어짐
        # print(*tmp)
        max_value = max(max_value, check()) #갯수 체크
print(max_value)