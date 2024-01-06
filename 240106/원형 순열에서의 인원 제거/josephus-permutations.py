from sys import stdin
n, k = list(map(int, stdin.readline().split()))
from collections import deque
base = deque()
for i in range(1, n+1):
    base.append(i)
result = []
idx = 1
while len(base) != 0:
    if idx%k != 0:
        base.append(base.popleft())
    else:
        result.append(base.popleft())
    idx+=1
print(*result)