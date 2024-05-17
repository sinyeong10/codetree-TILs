from sys import stdin
n, s = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

import sys
ans = sys.maxsize
total = sum(base)
for i in range(n):
    for j in range(i+1, n):
        ans = min(ans, abs(s-total+base[i]+base[j]))
print(ans)