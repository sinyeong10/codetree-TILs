from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

ans = 0
import sys
min_value = sys.maxsize
for i in range(n):
    min_value = min(min_value, base[i])
    tmp = base[i]-min_value
    if tmp > 0:
        ans = max(ans, tmp)
print(ans)