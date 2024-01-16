from sys import stdin
from sortedcontainers import SortedSet
n = int(stdin.readline())
base = SortedSet()

for _ in range(n):
    order = stdin.readline().split()
    if order[0] == "add":
        base.add(int(order[1]))
    elif order[0] == "remove":
        base.remove(int(order[1]))
    elif order[0] == "find":
        if int(order[1]) in base:
            print("true")
        else:
            print("false")
    elif order[0] == "lower_bound":
        idx = base.bisect_left(int(order[1]))
        if idx == len(base):
            print("None")
        else:
            print(base[idx])
    elif order[0] == "upper_bound":
        idx = base.bisect_right(int(order[1])) #없으면 원소의 갯수임!
        if idx == len(base):
            print("None")
        else:
            print(base[idx])
    elif order[0] == "largest":
        if len(base) == 0:
            print("None")
        else:
            print(base[-1])
    elif order[0] == "smallest":
        if len(base) == 0:
            print("None")
        else:
            print(base[0])