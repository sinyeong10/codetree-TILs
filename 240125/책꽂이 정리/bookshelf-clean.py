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

    def add(self, direct, node):
        if self.head == None:
            self.head = node
            self.tail = node
        elif direct == "tail":
            connect(self.tail, node)
            self.tail = self.tail.next
        elif direct == "head":
            connect(node, self.head)
            self.head = self.head.prev
        self.nodelen += 1

    def remove(self, node):
        if self.nodelen == 1:
            self.tail = None
            self.head = None
        elif self.head == node:
            self.head = self.head.next
            disconnect(self.head.prev, self.head)
        elif self.tail == node:
            self.tail = self.tail.prev
            disconnect(self.tail, self.tail.next)
        self.nodelen -= 1
        return node

bookcase_idx = [None]+[bookcase(i) for i in range(1, k+1)]


# node = Node(1)
# bookcase_idx[1].head = node
# bookcase_idx[1].tail = node
# bookcase_idx[1].nodelen = 1
for i in range(1, n+1):
    node = Node(i)
    bookcase_idx[1].add("tail", node)
    # connect(bookcase_idx[1].tail, node)
    # bookcase_idx[1].tail = bookcase_idx[1].tail.next
    # bookcase_idx[1].nodelen += 1
#     print(len(bookcase_idx[1]), end=" ")
# print()

for _ in range(q):
    order = list(map(int, stdin.readline().split())) #다 숫자라 숫자로 처리했음!
        
    # for i in range(1, k+1):
    #     print(len(bookcase_idx[i]), end=" ")
    #     node = bookcase_idx[i].head
    #     while node != None:
    #         print(node.data, end=" ")
    #         node = node.next
    #     print()

    i, j = order[1], order[2]
    if order[0] == 1:
        if bookcase_idx[i].head == None:
            continue
        bookcase_idx[j].add("tail", bookcase_idx[i].remove(bookcase_idx[i].head))
    elif order[0] == 2:
        if bookcase_idx[i].head == None:
            continue
        bookcase_idx[j].add("head", bookcase_idx[i].remove(bookcase_idx[i].tail))
    elif order[0] == 3:
        if bookcase_idx[i].head == None:
            continue
        node = bookcase_idx[i].tail
        n = len(bookcase_idx[i]) #값이 변할 수 있어서 미리 저장
        for _ in range(n):
            tmp, node = node, node.prev #remove시 관계가 사라지기에 미리 저장
            bookcase_idx[j].add("head", bookcase_idx[i].remove(tmp))
            # print(bookcase_idx[i].head.data, bookcase_idx[i].tail.data)
            # print(bookcase_idx[j].head.data, bookcase_idx[j].tail.data)
    elif order[0] == 4:
        if bookcase_idx[i].head == None:
            continue
        node = bookcase_idx[i].head
        n = len(bookcase_idx[i]) #값이 변할 수 있어서 미리 저장
        for _ in range(n):
            tmp, node = node, node.next #remove시 관계가 사라지기에 미리 저장
            bookcase_idx[j].add("tail", bookcase_idx[i].remove(tmp))

for i in range(1, k+1):
    print(len(bookcase_idx[i]), end=" ")
    node = bookcase_idx[i].head
    while node != None:
        print(node.data, end=" ")
        node = node.next
    print()


#구현하면서 오류를 고치다보니 뭐가 문제인지 확인하기도 어렵다....
# for _ in range(q):
#     order = list(map(int, stdin.readline().split())) #다 숫자라 숫자로 처리했음!
#     i, j = order[1], order[2]
#     if order[0] == 1:
#         if bookcase_idx[i].head is None: #변경할 값이 없으면 패스
#             continue

#         if len(bookcase_idx[j])==0: #들어갈 곳에 아무것도 없는 상태
#             bookcase_idx[j].head = bookcase_idx[i].head
#             bookcase_idx[j].tail = bookcase_idx[i].head
#         else:
#             connect(bookcase_idx[j].tail, bookcase_idx[i].head)
#             bookcase_idx[j].tail = bookcase_idx[j].tail.next

#         if i != j:
#             bookcase_idx[i].head = bookcase_idx[i].head.next
        
        
#         # print(bookcase_idx[i].head.data, bookcase_idx[i].tail.data)
#         # print(bookcase_idx[j].head.data, bookcase_idx[j].tail.data)
#         disconnect(bookcase_idx[j].tail, bookcase_idx[i].head)
#         bookcase_idx[j].nodelen += 1
#         bookcase_idx[i].nodelen -= 1
#     elif order[0] == 2:
#         if bookcase_idx[i].tail is None: #변경할 값이 없으면 패스
#             continue

#         if len(bookcase_idx[j])==0: #들어갈 곳에 아무것도 없는 상태
#             bookcase_idx[j].head = bookcase_idx[i].tail
#             bookcase_idx[j].tail = bookcase_idx[i].tail
#         else:
#             connect(bookcase_idx[i].tail, bookcase_idx[j].head)
#             bookcase_idx[j].head = bookcase_idx[j].head.prev

#         if i != j:
#             bookcase_idx[i].tail = bookcase_idx[i].tail.prev

#         disconnect(bookcase_idx[i].tail, bookcase_idx[j].head)
#         bookcase_idx[j].nodelen += 1
#         bookcase_idx[i].nodelen -= 1

#     elif order[0] == 3:
#         if bookcase_idx[i].head is None: #변경할 값이 없으면 패스
#             continue

#         if len(bookcase_idx[j])==0: #들어갈 곳에 아무것도 없는 상태
#             bookcase_idx[j].head = bookcase_idx[i].head
#             bookcase_idx[j].tail = bookcase_idx[i].tail
#         else:
#             connect(bookcase_idx[i].tail, bookcase_idx[j].head)

#         bookcase_idx[j].head = bookcase_idx[i].head
#         if i != j:
#             bookcase_idx[i].head = None
#             bookcase_idx[i].tail = None
#         else:
#             disconnect(bookcase_idx[i].tail, bookcase_idx[i].head)

#         len_value = len(bookcase_idx[i]) #i,j가 같을 수 있음
#         bookcase_idx[j].nodelen += len_value
#         bookcase_idx[i].nodelen -= len_value

#     elif order[0] == 4:
#         if bookcase_idx[i].head is None: #변경할 값이 없으면 패스
#             continue

#         if len(bookcase_idx[j])==0: #들어갈 곳에 아무것도 없는 상태
#             bookcase_idx[j].head = bookcase_idx[i].head
#             bookcase_idx[j].tail = bookcase_idx[i].tail
#         else:
#             connect(bookcase_idx[j].tail, bookcase_idx[i].head)

#         bookcase_idx[j].tail = bookcase_idx[i].tail
#         if i != j:
#             bookcase_idx[i].head = None
#             bookcase_idx[i].tail = None
#         else:
#             disconnect(bookcase_idx[i].tail, bookcase_idx[i].head)

#         len_value = len(bookcase_idx[i]) #i,j가 같을 수 있음
#         bookcase_idx[j].nodelen += len_value
#         bookcase_idx[i].nodelen -= len_value