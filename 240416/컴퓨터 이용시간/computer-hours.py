from sys import stdin
n = int(stdin.readline())

# seat = [0 for _ in range(n+1)]
find_seat = [False for _ in range(n)]

import heapq
#min-heaq
order = []

for i in range(n):
    heapq.heappush(order, i+1)

#heapq.heappop(order)

point = []
for i in range(n):
    p, q = list(map(int, stdin.readline().split()))
    point.append((p, +1, i))
    point.append((q, -1, i))

point.sort()

for value, direct, idx in point:
    # print("\n", value, direct, idx)
    if direct == 1:
        key = heapq.heappop(order)
        # seat[key] = idx #없어도 됨! 각 자리별 누가 쓰는지는 필요x
        find_seat[idx] = key
    else:
        heapq.heappush(order, find_seat[idx])
        # print(find_seat[idx])
    # print(order)

print(*find_seat)