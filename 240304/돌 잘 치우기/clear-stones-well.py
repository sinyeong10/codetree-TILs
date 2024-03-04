from sys import stdin
n,k,m = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
start = [] #처음 위치 저장!
for _ in range(k):
    r,c = list(map(int, stdin.readline().split()))
    start.append((r-1,c-1))


def in_range(x,y):
    return 0<=x<n and 0<=y<n

from collections import deque
def bfs():
    #매번 새로 설정하며 시작!
    q = deque()
    visited = [[False]*n for _ in range(n)]

    total = 0
    #모든 시작점을 다 q에 넣어서 처리함!
    for x, y in start:
        q.append((x,y))
        visited[x][y] = True #처음위치의 방문표시!
        total += 1
    
    dx, dy = [-1,1,0,0], [0,0,-1,1]

    while q:
        i,j = q.popleft()
        for dxs, dys in zip(dx,dy):
            next_i, next_j = i+dxs, j+dys
            #다음 위치가 범위 안이고, 갈 수 있으며, 아직 방문하지 않음
            if in_range(next_i, next_j) and base_2d[next_i][next_j] == 0 and not visited[next_i][next_j]:
                visited[next_i][next_j] = True
                total += 1
                q.append((next_i, next_j))
    return total            

# print(bfs())

stone = []
for i in range(n):
    for j in range(n):
        if base_2d[i][j] == 1:
            stone.append((i,j))

ans = []
def sol(idx, cnt): #현재 idx번 돌을보며 cnt갯수를 선택!
    tmp = 0
    if cnt == m: #m개의 돌이 선택되면 삭제 후 탐색하고 복구!
        for i in range(m): #돌 삭제
            x,y = stone[i]
            base_2d[x][y] = 0
        tmp = bfs()
        # print(ans, idx, cnt, tmp)
        for i in range(m): #돌 복구
            x,y = stone[i]
            base_2d[x][y] = 1
        return tmp
    
    if idx == len(stone): #cnt가 m이 아닌데 스톤을 다 봄
        return tmp #0반환

    sol(idx+1, cnt)
    ans.append(idx)
    tmp = max(tmp, sol(idx+1, cnt+1))
    ans.pop()
    return tmp
    
print(sol(0,0))