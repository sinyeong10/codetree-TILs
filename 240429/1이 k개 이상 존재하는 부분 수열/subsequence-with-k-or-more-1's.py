from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

import sys
ans = sys.maxsize
count = 0
end = 0
total = 0
for first in range(n):
    while end < n and count < k:
        if base[end] == 1:
            count += 1
        end += 1
        total += 1
    # print(base[first:end], first, end, count, total)
    if base[first] == 1 and count >= k:
        ans = min(ans, total)
        count -= 1
    total -= 1
print(ans if ans != sys.maxsize else -1)