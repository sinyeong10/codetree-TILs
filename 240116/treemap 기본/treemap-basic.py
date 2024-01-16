from sortedcontainers import SortedDict
from sys import stdin
n = int(stdin.readline())
sd = SortedDict()

for _ in range(n):
    order = stdin.readline().split()
    if order[0] == "add":
        sd[int(order[1])] = int(order[2])
    elif order[0] == "remove": #잘못된 경우는 없음
        sd.pop(int(order[1]))
    elif order[0] == "find":
        if int(order[1]) in sd:
            print(sd[int(order[1])])
        else:
            print("None")
    elif order[0] == "print_list":
        if len(sd) == 0:
            print("None")
        else:
            for elem in sd.values():
                print(elem, end=" ")
            print()