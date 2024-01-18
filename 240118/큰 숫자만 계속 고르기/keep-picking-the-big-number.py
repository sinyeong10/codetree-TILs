from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

import heapq
max_heap = []
for i in range(n):
    heapq.heappush(max_heap, -base[i])

for _ in range(m):
    max_num = -heapq.heappop(max_heap)-1 #최댓값에서 1뺌
    heapq.heappush(max_heap, -max_num) #다시 넣음

print(-max_heap[0])