from sys import stdin
n, m = list(map(int, stdin.readline().split()))

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s,e,v = list(map(int, stdin.readline().split()))
    graph[s][e] = v

# for elem in graph:
#     print(*elem)

dist = [float("inf") for _ in range(n+1)]
visited = [False for _ in range(n+1)]

#for문으로 최솟값을 찾아 다음 노드를 결정 O(V^2)
def dijkstra(node):
    dist[node] = 0
    for _ in range(n): #n개의 노드를 다 돎
        #가장 dist가 작은 정점을 찾음!
        min_index = -1
        for j in range(1, n+1):
            if visited[j]:
                continue
            #순서대로 일단 넣고 최소값인걸 체크 : 남은 게 다 무한대여도 처리가능!
            if min_index == -1 or dist[min_index] > dist[j]:
                min_index = j
        visited[min_index] = True

        for k in range(1, n+1):
            if graph[min_index][k] == 0: #연결이 없음! or 자기 자신임!
                continue
            dist[k] = min(dist[k], graph[min_index][k]+dist[min_index])
            
start = 1
dijkstra(start)
for idx in range(1,n+1):
    if idx == start:
        continue
    print(dist[idx])