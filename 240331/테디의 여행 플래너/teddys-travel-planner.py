from sys import stdin
n, q = list(map(int, stdin.readline().split()))
city = stdin.readline().split()

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

pick = Node(city[0])
tmp = pick
for i in range(1, n):
    node = Node(city[i])
    tmp.next = node
    node.prev = tmp
    tmp = tmp.next
tmp.next = pick
pick.prev = tmp

# for _ in range(n+2):
#     print(pick.data, end=" ")
#     pick = pick.next
# print()

#원형임! 아래는 
# pick = Node(city[-1])
# for i in range(n-1,-1,-1):
#     # print(i)
#     tmp = Node(city[i])
#     pick.prev = tmp
#     tmp.next = pick
#     pick = pick.prev
# print(pick.data)

# while pick != None:
#     print(pick.data, end=" ")
#     pick = pick.next
# print()

for _ in range(q):
    order = stdin.readline().split()
    if order[0] == "1":
        if pick.next != None:
            pick = pick.next
    elif order[0] == "2":
        if pick.prev != None:
            pick = pick.prev
    elif order[0] == "3":
        tmp = pick.next
        if tmp != None:
            pick.next = tmp.next
            if tmp.next != None:
                tmp.next.prev = pick
            tmp.next = tmp.prev = None
    elif order[0] == "4":
        tmp = pick.next
        pick.next = Node(order[1])
        pick.next.prev = pick

        if tmp != None:
            tmp.prev = pick.next
            pick.next.next = tmp

    # print(pick.prev, pick.data, pick.next)

    if pick.prev != pick.next: #순환구조이므로 prev와 next가 같으면 한개만 있는 것
        print(pick.prev.data, pick.next.data)
    else:
        print(-1)