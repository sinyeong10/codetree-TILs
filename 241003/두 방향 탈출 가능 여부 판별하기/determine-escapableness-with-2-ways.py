from sys import stdin
n, m = list(map(int, stdin.readline().split()))

base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
visit_2d = [[False for _ in range(m)] for _ in range(n)]

# print(base_2d)


def can_go(x,y): #x가 행, y가 열
    if not (0<=x<n and 0<=y<m): #범위 밖인 경우
        return False
    elif base_2d[x][y] == 0: #못가는 경우
        return False
    elif visit_2d[x][y]: #이미 방문한 경우
        return False
    else:
        return True

# print(can_go(0,0))

def dfs(x,y):
    dxs, dys = [1,0],[0,1]
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x+dx, y+dy
        if can_go(next_x, next_y):
            visit_2d[next_x][next_y] = True
            dfs(next_x, next_y)

visit_2d[0][0] = True
dfs(0,0)

print(1 if visit_2d[-1][-1] else 0)