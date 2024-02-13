from sys import stdin
n, m = list(map(int, stdin.readline().split()))
#번호 기준이라 1크게! #그래프와 최단 거리 테이블을 같이 처리!
dist = [[float("inf")]*(n+1) for _ in range(n+1)]
for _ in range(m):
    i,j,v = list(map(int, stdin.readline().split()))
    dist[i][j] = min(dist[i][j], v) #i,j가 같은데 v가 다를 수 있음!

for i in range(n+1):
    dist[i][i] = 0

# for elem in graph:
#     print(*elem)

for k in range(1,n+1): #이걸 거쳐가는 경우!
    for i in range(1,n+1): #시작 노드
        for j in range(1,n+1): #끝 노드
            if dist[i][j] > dist[i][k]+dist[k][j]:
                dist[i][j] = dist[i][k]+dist[k][j]

# for elem in dist[1:]:
#     print(*elem[1:])

for i in range(1, n+1):
    for j in range(1,n+1):
        if dist[i][j] == float("inf"):
            print(-1, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()