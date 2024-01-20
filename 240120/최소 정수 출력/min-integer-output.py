import heapq
from sys import stdin
n = int(stdin.readline())
hq = []
for _ in range(n):
    num = int(stdin.readline())
    if num == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
            
        continue
    
    heapq.heappush(hq, num)