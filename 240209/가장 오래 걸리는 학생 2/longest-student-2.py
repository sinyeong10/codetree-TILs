from sys import stdin
n, m = list(map(int, stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,v = list(map(int, stdin.readline().split()))
    #n번부터 dijkstra로 나머지 탐색으로 처리하기 위해서 방향을 뒤집음
    graph[e].append((v,s)) #heapq과 양식 맞추기 위해 가중치 먼저!

dist = [float("inf") for _ in range(n+1)]
dist[n] = 0

import heapq
hq = []
heapq.heappush(hq, (0, n))

while hq:
    min_dist, min_node = heapq.heappop(hq)

    if min_dist != dist[min_node]: #해당 노드의 수정이 일어남! #>일때 추가되므로 더 작은 값으로 이미 갱신된 것!
        continue
    
    for target_dist, target_node in graph[min_node]:
        new_dist = dist[min_node]+target_dist #min_node를 거쳐 target_node로!
        if dist[target_node] > new_dist:
            dist[target_node] = new_dist #값 갱신
            heapq.heappush(hq, (new_dist, target_node)) #다음에 체크!

print(max(dist[1:]))