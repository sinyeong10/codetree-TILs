from sys import stdin
n, m = list(map(int, stdin.readline().split()))
k = int(stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,v = list(map(int, stdin.readline().split()))
    graph[s].append((v,e)) #가중치와 가는 위치, heapq의 우선순위처리와 같은 방식으로 입력!
    graph[e].append((v,s)) #무방향그래프라서 반대도 입력!

# print(graph)

dist = [float("inf") for _ in range(n+1)]
dist[k] = 0

import heapq
hq = []
heapq.heappush(hq, (0, k)) #처음 위치 들어감!

while hq:
    min_dist, min_node = heapq.heappop(hq)

    if min_dist != dist[min_node]: #갱신이 되었다면 패스
        continue

    #graph와 heapq에 들어가는 튜플의 순서가 맞는지 확인!
    for target_dist, target_node in graph[min_node]: #선택된 곳에서 갈 수 있는 곳을 전부 봄
        # print(min_dist, min_node, target_dist, target_node)
        new_dist = dist[min_node]+target_dist #min_node를 거쳐 target_node로 감
        if dist[target_node] > new_dist: #거쳐가는 게 더 최단 경로!
            dist[target_node] = new_dist
            heapq.heappush(hq, (new_dist, target_node)) #최단 경로로 갱신되었기에 여기서부터 다른 곳을 갈 때 최단 거리일 수 있음
    # print(dist)

for i in range(1, n+1):
    print(dist[i] if dist[i] != float("inf") else -1)