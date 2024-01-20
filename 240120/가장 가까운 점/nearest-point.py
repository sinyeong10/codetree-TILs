from sys import stdin
n, m = list(map(int, stdin.readline().split()))

import heapq
hq = []
for _ in range(n):
    x, y = list(map(int, stdin.readline().split()))
    heapq.heappush(hq, (abs(x)+abs(y), x, y))

for _ in range(m):
    _, x, y = heapq.heappop(hq)
    x, y = x+2, y+2
    heapq.heappush(hq, (abs(x)+abs(y), x, y))

print(hq[0][1], hq[0][2])