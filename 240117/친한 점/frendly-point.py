from sys import stdin
n, m = list(map(int, stdin.readline().split()))

from sortedcontainers import SortedSet
base = SortedSet()
for _ in range(n):
    x, y = list(map(int, stdin.readline().split()))
    base.add((x, y))

for _ in range(m):
    x, y = list(map(int, stdin.readline().split()))
    idx = base.bisect_left((x, y))
    if idx == len(base):
        print(-1, -1)
    else:
        print(*base[idx])