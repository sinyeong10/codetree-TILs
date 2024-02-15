from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
town = []
visited = [[False]*n for _ in range(n)] #방문여부

def can_go(i,j):
    if not(0<=i<n and 0<=j<n):
        return False
    if visited[i][j] or base_2d[i][j] == 0: #이미 방문했거나 벽이 있어서 못감
        return False
    return True


dx, dy = [-1,1,0,0], [0,0,-1,1]

def dfs(i, j):
    visited[i][j] = True
    total = 1
    for dxs, dys in zip(dx, dy):
        next_i, next_j = i+dxs, j+dys
        if can_go(next_i, next_j): #갈수 있다면
            total += dfs(next_i, next_j)
    return total

for i in range(n):
    for j in range(n):
        if not visited[i][j] and base_2d[i][j] ==  1: #미방문, 마을
            town.append(dfs(i,j))
town.sort()

print(len(town))
for elem in town:
    print(elem)