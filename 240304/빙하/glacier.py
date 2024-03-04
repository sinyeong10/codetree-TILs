from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

def in_range(i,j): #i행 j열
    return 0<=i<n and 0<=j<m

# from collections import deque
# def bfs():
#     visited = [[False]*m for _ in range(n)] #매번 방문 배열을 갱신!
#     #매번 방문 배열을 갱신하는 대신 이번 턴 빙하를 모두 시작 지에 넣으면 갱신 없이도 가능!, 모든 빙하를 시작점에 넣었기에 visited 배열한 것이 초기화하는 의미가 됨!
#     q=deque()
#     #초기값으로 0,0을 줌 조건상 바깥쪽을 전부 갈 수 있음!
#     q.append((0,0))
#     visited[0][0] = True

#     dx, dy = [-1,1,0,0], [0,0,-1,1]
#     total = 0
#     while q:
#         x, y = q.popleft()
#         for dxs, dys in zip(dx, dy):
#             next_x, next_y = x+dxs, y+dys
#             if in_range(next_x, next_y) and not visited[next_x][next_y]:
#                 if base_2d[next_x][next_y] == 0: #빙하가 아니면 갈 수 있음!
#                     visited[next_x][next_y] = True
#                     q.append((next_x, next_y))
#                 else: #빙하인 경우!, 여기서 추가로 더 가지 않음!
#                     visited[next_x][next_y] = True
#                     base_2d[next_x][next_y] = 0 #다음 BFS에서는 갈 수 있음!
#                     total += 1 #가장 외곽의 빙하의 갯수
#     return total

# t = 0
# while True:
#     tmp = bfs()
#     if tmp == 0: #다 녹았으면 이전 상태를 출력하고 종료!
#         print(t, ans)
#         break
#     ans = tmp
#     t += 1
    
#     #검증용
#     # print(t)
#     # for elem in base_2d:
#     #     print(*elem)



from collections import deque
def bfs():
    visited = [[False]*m for _ in range(n)]
    #매번 방문 배열을 갱신하는 대신 이번 턴 빙하를 모두 시작지에 넣으면 갱신 없이도 가능!, 모든 빙하를 시작점에 넣었기에 visited 배열한 것이 초기화하는 의미가 됨!
    q=deque()
    #초기값으로 0,0을 줌 조건상 바깥쪽을 전부 갈 수 있음!
    q.append((0,0))
    visited[0][0] = True

    t = 0
    ans = 0
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    while True:
        # print(t, q)
        tmp = deque()
        total = 0
        while q:
            x, y = q.popleft()
            for dxs, dys in zip(dx, dy):
                next_x, next_y = x+dxs, y+dys
                if in_range(next_x, next_y) and not visited[next_x][next_y]:
                    if base_2d[next_x][next_y] == 0: #빙하가 아니면 갈 수 있음!
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))
                    else: #빙하인 경우!, 여기서 추가로 더 가지 않음!
                        visited[next_x][next_y] = True
                        tmp.append((next_x, next_y)) #다음 BFS에서는 갈 수 있음!
                        total += 1 #가장 외곽의 빙하의 갯수
        if total == 0:
            return t, ans
        ans = total
        t += 1
        q = tmp

print(*bfs())