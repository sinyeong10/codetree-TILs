from sys import stdin
from collections import deque #앞에서 수정(삭제가 일어난 다는 것에서 활용)
n = int(stdin.readline())
base = deque()
for i in range(1, n+1):
    base.append(i)

while len(base) != 1:
    base.popleft()
    base.append(base.popleft())
print(base[0])