from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

def can_go(i,j):
    if not(0<=i<n and 0<=j<n):
        return False
    if visited[i][j] or base_2d[i][j] == 1:
        return False
    return True

from collections import deque
dx, dy = [-1,1,0,0], [0,0,-1,1]
q = deque()
visited = [[False]*n for _ in range(n)] #다른 시작위치에서 같은 곳 이동하면 한번만 처리됨!

def bfs():
    total = 1 #처음의 자기자신!

    while q:
        x,y = q.popleft() #앞을 뺌
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if can_go(next_x, next_y):
                #들어갈 때 관련 처리를 다함!
                visited[next_x][next_y] = True
                total += 1
                q.append((next_x,next_y))
    return total

#매번 처리하지 말고 큐에 한번에 넣고 처리해도 가능!
for _ in range(k):
    r, c = list(map(int, stdin.readline().split()))
    q.append((r-1,c-1))
    visited[r-1][c-1] = True #처음의 자기자신도 반드시 방문처리를 해줘야함!
print(bfs())




# ans = 0
# for _ in range(k):
#     r, c = list(map(int, stdin.readline().split()))
#     r,c = r-1,c-1 #인덱스로
#     if visited[r][c]: #이미 방문시 넘어감
#         continue
#     q.append((r,c))
#     visited[r][c] = True #처음의 자기자신도 반드시 방문처리를 해줘야함!
#     ans += bfs()
# print(ans)