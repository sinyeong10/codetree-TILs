from sys import stdin
n = int(stdin.readline())
q = int(stdin.readline())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

base = {}
for i in range(1, n+1):
    base[i] = Node(i)

for _ in range(q):
    order = stdin.readline().split()
    if order[0] == "1":
        i = int(order[1])
        if base[i].next is not None:
            base[i].next.prev = base[i].prev
        if base[i].prev is not None:
            base[i].prev.next = base[i].next

        base[i].next = None
        base[i].prev = None
    elif order[0] == "2":
        i, j = int(order[1]), int(order[2])
        if base[i].prev is not None:
            base[i].prev.next = base[j]
            base[j].prev = base[i].prev

        base[j].next = base[i]
        base[i].prev = base[j]
    elif order[0] == "3":
        i, j = int(order[1]), int(order[2])
        if base[i].next is not None:
            base[i].next.prev = base[j]
            base[j].next = base[i].next
        
        base[j].prev = base[i]
        base[i].next = base[j]
    elif order[0] == "4":
        i = int(order[1])
        a, c = base[i].prev, base[i].next
        if a is not None:
            a = a.data
        else:
            a = 0
        if c is not None:
            c = c.data
        else:
            c = 0
        print(a, c)

    # for i in range(1, n+1):
    #     tmp = base[i].prev
    #     if tmp is not None:
    #         tmp = tmp.data
    #     else:
    #         tmp = 0
    #     print("[",tmp, end=" ")
    #     print(base[i].data, end=" ")
    #     tmp = base[i].next
    #     if tmp is not None:
    #         tmp = tmp.data
    #     else:
    #         tmp = 0
    #     print(tmp, "]", end=" ")
    # print()


for i in range(1, n+1):
    tmp = base[i].next
    if tmp is not None:
        tmp = tmp.data
    else:
        tmp = 0
    print(tmp, end=" ")