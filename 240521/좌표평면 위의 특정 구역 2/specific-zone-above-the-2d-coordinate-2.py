from sys import stdin
n = int(stdin.readline())
point = [list(map(int, stdin.readline().split())) for _ in range(n)]

import sys
ans = sys.maxsize
for i in range(n):
    min_x, min_y = sys.maxsize, sys.maxsize
    max_x, max_y = 0, 0
    for j in range(n):
        if i == j:
            continue
        x, y = point[j]
        min_x = min(min_x,x)
        max_x = max(max_x,x)
        min_y = min(min_y,y)
        max_y = max(max_y,y)
    ans = min(ans, (max_x-min_x)*(max_y-min_y))
print(ans)