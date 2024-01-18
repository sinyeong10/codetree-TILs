from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

import heapq
max_heap = []
for i in range(n):
    heapq.heappush(max_heap, -base[i])

for _ in range(m):
    heapq.heappush(max_heap, -(-heapq.heappop(max_heap)-1))

print(-max_heap[0])