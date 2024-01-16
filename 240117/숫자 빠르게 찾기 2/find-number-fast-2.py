from sys import stdin
n, m = list(map(int, stdin.readline().split()))
from sortedcontainers import SortedSet
base = SortedSet(list(map(int, stdin.readline().split())))
for _ in range(m):
    num = int(stdin.readline())
    idx = base.bisect_left(num)
    if idx == n:
        print(-1)
    else:
        print(base[idx])