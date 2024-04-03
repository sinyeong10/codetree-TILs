from sys import stdin
n, m, q = list(map(int, stdin.readline().split()))

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None #반시계 방향!
        self.next = None #시계 방향!

def connect(s,e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

node_find = {}
##circles = [-1 for _ in range(n+1)] #각 노드가 속한 원의 최소값!

##매 명령마다 처리하는 것 보다 마지막에 처리하는 게 효율적! 어차피 전부 봐야해서!

for i in range(m):
    circle = list(map(int, stdin.readline().split()))

    key = min(circle[1:])
    ##circles[circle[1]] = key

    node_find[circle[1]] = Node(circle[1])
    head = node_find[circle[1]]
    tail = head

    for j in range(circle[0]-1):
        node_find[circle[j+2]] = Node(circle[j+2])
        connect(tail, node_find[circle[j+2]])
        tail = tail.next

        ##circles[circle[j+2]] = key
    
    connect(tail, head)

# print(circles)

for _ in range(q):
    order = list(map(int, stdin.readline().split()))
    if order[0] == 1:
        a, b = node_find[order[1]], node_find[order[2]]
        ##
        # if circles[a.data] < circles[b.data]: #a가 더 작음!
        #     key = circles[a.data]

        #     head = b
        #     circles[head.data] = key
        #     head = head.next
        #     while head != b:
        #         circles[head.data] = key
        #         head = head.next

        # elif circles[a.data] > circles[b.data]: #b가 더 작음!
        #     key = circles[b.data]

        #     head = a
        #     circles[head.data] = key
        #     head = head.next
        #     while head != a:
        #         circles[head.data] = key
        #         head = head.next
        ##
        connect(b.prev, a.next)
        connect(a, b)

    elif order[0] == 2:
        a, b = node_find[order[1]], node_find[order[2]]
        ##
        # key = a.data
        # tail = a
        # if tail != b:
        #     tail = tail.next
        #     key = min(key, tail.data)
        ##
    
        # print("2번 명령 체크")
        # print(a.prev.data, b.data, "\\", b.prev.data, a.data)
        # print(a.prev.data, a.next.data)
        # print(b.prev.data, b.next.data)
        tmp = b.prev
        connect(a.prev, b)
        # connect(b.prev, a) #b가 수정된 시점이라 문제!
        connect(tmp, a) #tmp에 저장해줬다가 처리!
        # print(a.prev.data, a.next.data)
        # print(b.prev.data, b.next.data)

        ##
        # if key > circles[a.data]: #b그룹이 더 작아짐. #a그룹은 key로 갱신!
        #     head = a
        #     circles[head.data] = key
        #     head = head.next
        #     while head != a:
        #         circles[head.data] = key
        #         head = head.next
        # elif key < circles[a.data]: #a그룹이 더 작아짐, b그룹은 재계산하여 갱신!
        #     tail = b
        #     new_key = b.data
        #     tail = tail.next
        #     while tail != b:
        #         tail = tail.next
        #         new_key = min(new_key, tail.data)

        #     head = b
        #     circles[head.data] = new_key
        #     head = head.next
        #     while head != b:
        #         circles[head.data] = new_key
        #         head = head.next
        ##
    elif order[0] == 3:
        a = node_find[order[1]]
        ##
        # head = node_find[circles[a.data]]
        # print(head.data, end=" ")
        # head = head.prev
        # while head != node_find[circles[a.data]]:
        #     print(head.data, end=" ")
        #     head = head.prev
        # print()
        ##

        #가장 작은 위치 탐색
        key = a.data
        head = a
        head = head.next
        while head != a:
            key = min(key, head.data)
            head = head.next
        #해당위치부터 반시계방향으로 돌며 출력
        head = node_find[key]
        print(head.data, end=" ")
        head = head.prev
        while head != node_find[key]:
            print(head.data, end=" ")
            head = head.prev
        print()
        
    # print(order, circles)