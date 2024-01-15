from sys import stdin
n = int(stdin.readline())
base = {}
for _ in range(n):
    order = stdin.readline().split()

    if order[0] == "add":
        base[order[1]] = order[2]
    elif order[0] == "remove":
        base.pop(order[1])
    elif order[0] == "find":
        if order[1] in base:
            print(base[order[1]])
        else:
            print("None")