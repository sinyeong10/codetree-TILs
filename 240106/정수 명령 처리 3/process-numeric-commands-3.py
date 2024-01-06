from sys import stdin
from collections import deque
base = deque()
n = int(stdin.readline())
for _ in range(n):
    order = stdin.readline().split()
    if order[0] == "push_front": #앞이 left로 처리됨
        base.appendleft(order[1])
    elif order[0] == "push_back":
        base.append(order[1])
    elif order[0] == "pop_front":
        print(base.popleft())
    elif order[0] == "pop_back":
        print(base.pop())
    elif order[0] == "size":
        print(len(base))
    elif order[0] == "empty":
        print(1 if not base else 0)
    elif order[0] == "front":
        print(base[0])
    elif order[0] == "back":
        print(base[-1])