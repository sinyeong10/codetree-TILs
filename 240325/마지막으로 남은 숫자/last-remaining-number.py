from sys import stdin
import heapq

n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
hq = []

for i in range(n):
    heapq.heappush(hq, -base[i])

while len(hq) >= 2:
    a = -heapq.heappop(hq)
    b = -heapq.heappop(hq)
    # print(a,b)

    if a != b:
        heapq.heappush(hq, -abs(a-b))

if hq:
    print(-hq[0])
else:
    print(-1)