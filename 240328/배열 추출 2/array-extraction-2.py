from sys import stdin
n = int(stdin.readline())
import heapq
hq = []
for _ in range(n):
    x = int(stdin.readline())
    if x == 0:
        if hq:
            _, num = heapq.heappop(hq)
            print(num)
        else:
            print(0)
    else:
        heapq.heappush(hq, (abs(x), x))