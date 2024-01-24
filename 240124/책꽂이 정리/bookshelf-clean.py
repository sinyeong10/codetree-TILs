from sys import stdin
n, k = list(map(int, stdin.readline().split()))
q = int(stdin.readline())

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
def connect(a,b): #a,b를 연결
    if a is not None:
        a.next = b
    if b is not None:
        b.prev = a

def disconnect(a,b): #a,b의 연결을 끊음
    if a is not None:
        a.next = None
    if b is not None:
        b.prev = None

class bookcase:
    def __init__(self, number):
        self.number = number
        self.head = None
        self.tail = None
        self.nodelen = 0
    
    def __len__(self):
        return self.nodelen

bookcase_idx = [None]+[bookcase(i) for i in range(1, k+1)]

for i in range(1, n+1):
    node = Node(i)
    if len(bookcase_idx[1]) == 0:
        bookcase_idx[1].head = node
        bookcase_idx[1].tail = node
        bookcase_idx[1].nodelen = 1
    else:
        connect(bookcase_idx[1].tail, node)
        bookcase_idx[1].tail = bookcase_idx[1].tail.next
        bookcase_idx[1].nodelen += 1

    # print(len(bookcase_idx[1]), end=" ")
# print()

for _ in range(q):
    order = list(map(int, stdin.readline().split()))
    i, j = order[1], order[2]
    if order[0] == 1:
        if len(bookcase_idx[j])==0:
            bookcase_idx[j].head = bookcase_idx[i].head
            bookcase_idx[j].tail = bookcase_idx[i].head
        else:
            connect(bookcase_idx[j].tail, bookcase_idx[i].head)
        
        if bookcase_idx[i].head is not None:
            bookcase_idx[i].head = bookcase_idx[i].head.next
            bookcase_idx[j].tail = bookcase_idx[j].tail.next
            disconnect(bookcase_idx[j].tail, bookcase_idx[i].head)
            bookcase_idx[j].nodelen += 1
            bookcase_idx[i].nodelen -= 1
    elif order[0] == 2:
        if len(bookcase_idx[j])==0:
            bookcase_idx[j].head = bookcase_idx[i].tail
            bookcase_idx[j].tail = bookcase_idx[i].tail
        else:
            connect(bookcase_idx[i].tail, bookcase_idx[j].head)

        if bookcase_idx[i].tail is not None:
            bookcase_idx[i].tail = bookcase_idx[i].tail.prev
            bookcase_idx[j].head = bookcase_idx[j].head.prev
            disconnect(bookcase_idx[i].tail, bookcase_idx[j].head)
            bookcase_idx[j].nodelen += 1
            bookcase_idx[i].nodelen -= 1
    elif order[0] == 3:
        if len(bookcase_idx[j])==0:
            bookcase_idx[j].head = bookcase_idx[i].tail
            bookcase_idx[j].tail = bookcase_idx[i].tail
        else:
            connect(bookcase_idx[i].tail, bookcase_idx[j].head)

        if bookcase_idx[i].tail is not None:
            bookcase_idx[j].nodelen += len(bookcase_idx[i])
            bookcase_idx[i].nodelen = 0
            bookcase_idx[i].tail = bookcase_idx[i].tail.prev
            bookcase_idx[j].head = bookcase_idx[j].head.prev
        
    elif order[0] == 4:
        if len(bookcase_idx[j])==0:
            bookcase_idx[j].head = bookcase_idx[i].head
            bookcase_idx[j].tail = bookcase_idx[i].head
        else:
            connect(bookcase_idx[j].tail, bookcase_idx[i].head)

        if bookcase_idx[i].head is not None:
            bookcase_idx[j].nodelen += len(bookcase_idx[i])
            bookcase_idx[i].nodelen = 0
            bookcase_idx[i].head = bookcase_idx[i].head.next
            bookcase_idx[j].tail = bookcase_idx[j].tail.next

for i in range(1, k+1):
    print(len(bookcase_idx[i]), end=" ")
    node = bookcase_idx[i].head
    while node != None:
        print(node.data, end=" ")
        node = node.next
    print()