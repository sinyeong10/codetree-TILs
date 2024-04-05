from sys import stdin
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

node_find = {1 : Node(1)}
count = 2

def connect(s, e):
    if s is not None:
        s.next = e
    if e != None:
        e.prev = s

q = int(stdin.readline())
for _ in range(q):
    order = list(map(int, stdin.readline().split()))
    if order[0] == 1:
        node_find[count] = Node(count)
        semi_tail = node_find[count]
        count += 1
        semi_head = semi_tail
        for _ in range(order[2]-1):
            node_find[count] = Node(count)
            connect(semi_tail, node_find[count])
            semi_tail = semi_tail.next
            count += 1
        
        #뒤에 연결
        connect(semi_tail, node_find[order[1]].next)
        connect(node_find[order[1]], semi_head)


    elif order[0] == 2:
        node_find[count] = Node(count)
        semi_tail = node_find[count]
        count += 1
        semi_head = semi_tail
        for _ in range(order[2]-1):
            node_find[count] = Node(count)
            connect(semi_tail, node_find[count])
            semi_tail = semi_tail.next
            count += 1
        
        #앞에 연결
        connect(node_find[order[1]].prev, semi_head)
        connect(semi_tail, node_find[order[1]])

    elif order[0] == 3:
        a, b = node_find[order[1]].prev, node_find[order[1]].next
        if a is None or b == None:
            print(-1)
        else:
            print(a.data, b.data)

    # else:
    #     print(order[0], "error\n\n")    
    #
    # print(order[0], end = " : ")
    # head = node_find[1]
    # while head.prev != None:
    #     head = head.prev
    # while head != None:
    #     print(head.data, end = " ")
    #     head = head.next
    # print()