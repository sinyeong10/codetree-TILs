from sys import stdin
n, m = list(map(int, stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,v = list(map(int, stdin.readline().split()))
    #양방향 간선!
    graph[s].append((v, e))
    graph[e].append((v, s))
a,b = list(map(int, stdin.readline().split()))

import heapq
hq = []
heapq.heappush(hq, (0,a)) #시작점 들어감!
dist = [float("inf") for _ in range(n+1)]
dist[a] = 0
path = [-1 for _ in range(n+1)]

while hq:
    min_dist, min_node = heapq.heappop(hq)

    if min_dist != dist[min_node]: #이전에 수정됨!
        continue

    for target_dist, target_node in graph[min_node]: #min_node를 거쳐감!
        new_dist = min_dist + target_dist
        if dist[target_node] > new_dist:
            dist[target_node] = new_dist
            path[target_node] = min_node
            heapq.heappush(hq, (new_dist, target_node)) #최단 경로로 갱신되어 다시 살펴봄!

# print(dist)
# print(path)

answer = []
answer.append(b)

while b != a:
    b = path[b]
    answer.append(b)

print(*answer[::-1])