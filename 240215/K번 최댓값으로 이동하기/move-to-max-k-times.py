from sys import stdin
from collections import deque
q = deque()
n, k = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
r,c = list(map(int, stdin.readline().split()))
r,c = r-1,c-1 #인덱스로!

def can_go(x,y, elem, visited):
    if not(0<=x<n and 0<=y<n):
        return False
    if visited[x][y] or base_2d[x][y] >= elem:
        return False
    return True

dx, dy = [-1,1,0,0], [0,0,-1,1] #행번호 작은 게 먼저 나와야함... #여기서 처리는 힘듦...

def bfs(i, j):
    visited = [[False]*n for _ in range(n)]
    q.append((i, j))
    visited[i][j] = True
    elem = base_2d[i][j]

    max_value = 0
    index = (i,j)
    while q:
        x,y = q.popleft()
        # print(x,y)

        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if can_go(next_x, next_y, elem, visited):
                visited[next_x][next_y] = True
                q.append((next_x, next_y))
                
                # #처음은 제외하고 계산해야해서 다음에 갈 곳에서 체크!
                # if max_value < base_2d[next_x][next_y]:
                #     # print("갱신됨!", x,y,base_2d[next_x][next_y])
                #     index = (next_x, next_y)
                #     max_value = base_2d[next_x][next_y]
                # #값이 같은 경우!
                # elif max_value == base_2d[next_x][next_y]:
                #     x1, x2 = index
                #     #행번호가 더 작은 걸로 감!
                #     if x1 > next_x:
                #         index = (next_x, next_y)
                #     #행번호가 같으면 열번호가 더 작은 걸로 감!
                #     if x1 == next_x and x2 > next_y:
                #         index = (next_x, next_y)

                if max_value < base_2d[next_x][next_y]:
                    #튜플로 비교할 수 있음! (값, -행, -열)의 순서로 큰 것!
                    if (max_value, index[0], index[1]) < (base_2d[next_x][next_y], next_x, next_y):
                        max_value = base_2d[next_x][next_y]
                        index = (next_x, next_y)
    return index



#자신보다 작은 인접한 곳으로 이동하여 갈 수 있는 가장 큰 곳
#가장 작은 i, 그리고 가장 작은 j로

for i in range(k):
    r,c = bfs(r,c)
    # print(i, r,c)
print(r+1,c+1) #인덱스에서 번째로!