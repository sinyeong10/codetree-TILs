from sys import stdin
from sortedcontainers import SortedSet
T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    base = SortedSet()
    for _ in range(k):
        order = stdin.readline().split()
        if order[0] == "I":
            base.add(int(order[1]))
        elif order[0] == "D":
            if len(base) == 0:
                continue
            base.remove(base[-1 if int(order[1]) == 1 else 0]) #1시 최댓값 -1위치 삭제, -1시 최솟값 0위치 삭제
        # print(base)
    if len(base)==0:
        print("EMPTY")
    else:
        print(base[-1], base[0])