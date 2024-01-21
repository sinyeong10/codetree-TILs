from sys import stdin
S_init = stdin.readline().strip()
n = int(stdin.readline())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

base = Node(S_init)

for _ in range(n):
    order = stdin.readline().split()
    if order[0] == "1":
        node = Node(order[1])
        
        if base.prev is not None:
            base.prev.next = node
            node.prev = base.prev
        
        base.prev = node
        node.next = base
    elif order[0] == "2":
        node = Node(order[1])

        if base.next is not None:
            base.next.prev = node
            node.next = base.next
        
        base.next = node
        node.prev = base
    elif order[0] == "3":
        if base.prev is not None:
            base = base.prev
    elif order[0] == "4":
        if base.next is not None:
            base = base.next
        
    a, b, c = base.prev, base, base.next
    if a is not None:
        a = a.data
    else:
        a = "(Null)"
    b = b.data
    if c is not None:
        c = c.data
    else:
        c = "(Null)"
    print(a, b, c)