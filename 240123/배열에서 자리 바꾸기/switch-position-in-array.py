from sys import stdin
n = int(stdin.readline())
q = int(stdin.readline())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.Next = None

#초기 세팅
base = [None]+[Node(i) for i in range(1, n+1)]+[None]
head = base[1]
tail = base[n]

for i in range(1, n+1):
    base[i].prev = base[i-1]
    base[i].next = base[i+1]


def connect(a,b):
    if a is not None:
        a.next = b
    if b is not None:
        b.prev = a

for _ in range(q):
    a,b,c,d = list(map(int, stdin.readline().split()))

    tmp1 = (base[a].prev, base[b].next)
    tmp2 = (base[c].prev, base[d].next) #분리하는 시점에서 b 이후에 c가 오면 이후에 붙을 위치가 겹침..

    #분리
    #connect(base[a].prev, base[b].next)
    if base[a].prev is not None:
        base[a].prev.next = base[b].next
    if base[b].next is not None:
        base[b].next.prev = base[a].prev
    
    base[a].prev = base[b].next = None

    #분리
    #connect(base[c].prev, base[d].next)
    if base[c].prev is not None:
        base[c].prev.next = base[d].next
    if base[d].next is not None:
        base[d].next.prev = base[c].prev
    
    base[c].prev = base[d].next = None

    #tmp1연결
    #connect(tmp1[0], base[c])
    if tmp1[0] is not None:
        tmp1[0].next = base[c]
    base[c].prev = tmp1[0]

    #connect(base[d], tmp1[1])
    if tmp1[1] is not None:
        tmp1[1].prev = base[d]
    base[d].next = tmp1[1]

    #tmp2연결
    #connect(base[b], tmp2[1])
    if tmp2[1] is not None:
        tmp2[1].prev = base[b]
    base[b].next = tmp2[1]

    #connect(tmp2[0], base[a])
    if tmp2[0] is not None:
        tmp2[0].next = base[a]
    base[a].prev = tmp2[0]
        
while head != None:
    print(head.data, end=" ")
    head = head.next