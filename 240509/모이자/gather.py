from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

import sys
ans = sys.maxsize
for center in range(n):
    dist = 0
    for i in range(n):
        dist += abs(center-i)*base[i]
    ans = min(ans, dist)
    # print(center, dist)
print(ans)