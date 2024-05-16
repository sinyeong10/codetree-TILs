from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base_2d = [stdin.readline().strip() for _ in range(n)]

def in_range(i, j):
    return 0<=i<n and 0<=j<m

def check(i,j):
    dxs, dys = [-1,1,0,0,-1,1,1,-1], [0,0,-1,1,1,1,-1,-1] #상하좌우,우상우하좌하좌상
    tmp = 0
    for dx, dy in zip(dxs, dys):
        #i자리에 j로 오타...
        if in_range(i+dx, j+dy) and in_range(i+dx*2, j+dy*2) and base_2d[i+dx][j+dy] == base_2d[i+dx*2][j+dy*2] == "E":
            tmp += 1
    return tmp

cnt=0
for i in range(n):
    for j in range(m):
        if base_2d[i][j] == "L":
            cnt += check(i,j)
print(cnt)