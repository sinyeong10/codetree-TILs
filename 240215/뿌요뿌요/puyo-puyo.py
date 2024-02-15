from sys import stdin
import sys
sys.setrecursionlimit(10**8)
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

def can_go(x,y, elem):
    if not(0<=x<n and 0<=y<n):
        return False
    if visited[x][y] or base_2d[x][y] != elem: #이미 방문했거나 다른 숫자인 경우
        return False
    return True

dx,dy = [-1,1,0,0],[0,0,-1,1]

def dfs(i,j, elem):
    visited[i][j] = True
    total = 1 #자기 자신 선택
    for dxs, dys in zip(dx, dy):
        next_i, next_j = i+dxs, j+dys
        if can_go(next_i, next_j, elem):
            total += dfs(next_i, next_j, elem)
    return total

max_value = 0
total = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]: #아직 방문하지 않음
            tmp = dfs(i,j, base_2d[i][j])
            max_value = max(max_value, tmp)
            if tmp >= 4:
                total += 1
print(total, max_value)