from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x, y):
    visited[x][y] = True

    if (x, y) == (n-1, m-1):
        return True

    dx, dy = [1, 0], [0, 1] #하, 우
    for dxs, dys in zip(dx, dy):
        next_x, next_y = x+dxs, y+dys
        if in_range(next_x, next_y) and base[next_x][next_y] == 1: #이동 가능
            if dfs(next_x, next_y):
                return True
    
    return False
    


print(1 if dfs(0,0) else 0)