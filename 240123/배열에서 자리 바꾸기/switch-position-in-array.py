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
    if base[c] == head:
        head = base[a]
    elif base[a] == head:
        head = base[c]

    #<a,b>,<c,d>가 인접한 경우 좌우 노드 저장시 같은 노드가 겹칠 수 있음
    if base[b].next == base[c]:
        # print("A")
        #<c,d>를 <a,b>앞으로 보냄
        connect(base[c].prev, base[d].next) #구간 빼냄
        connect(base[a].prev, base[c]) #있으면 a.prev의 뒤에 연결
        connect(base[d], base[a]) #a의 앞에 연결
    elif base[d].next == base[a]:
        # print("B")
        #<a,b>를 <c,d>앞으로 보냄
        connect(base[a].prev, base[b].next) #구간 빼냄
        connect(base[c].prev,base[a])
        connect(base[b],base[c])
        
    else:
        # print("C")
        start = base[c].prev
        end = base[d].next
        #<c,d>를 <a,b>앞으로 보냄
        connect(base[c].prev, base[d].next) #구간 빼냄
        connect(base[a].prev, base[c]) #있으면 a.prev의 뒤에 연결
        connect(base[d], base[a]) #a의 앞에 연결

        #<a,b>를 <c,d>자리에 넣음
        connect(base[a].prev, base[b].next)
        connect(start,base[a])
        connect(base[b],end)

# q=head
while head != None:
    print(head.data, end=" ")
    head = head.next
# print()
# head=q