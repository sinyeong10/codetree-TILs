from sys import stdin
n = int(stdin.readline())
base = set()
for _ in range(n):
    order = stdin.readline().split()
    if order[0] == "add":
        base.add(int(order[1])) #중복된 값은 알아서 무시됨
    elif order[0] == "remove":
        base.remove(int(order[1]))
    elif order[0] == "find":
        if int(order[1]) in base:
            print("true")
        else:
            print("false")