import heapq
from sys import stdin
n = int(stdin.readline())
hq = []
for _ in range(n):
    x = int(stdin.readline())

    if x > 0:
        heapq.heappush(hq, -x)
    else:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)