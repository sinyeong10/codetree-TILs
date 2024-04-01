from sys import stdin
n, m, q = list(map(int, stdin.readline().split()))

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def connect(s,e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

lines = [None for _ in range(m)]
people_line = [-1 for _ in range(n+1)] #모든 노드는 유일하며 2개이상의 줄을 서지 않기 때문에 필요없다고 생각했으나 노드 수정시 시작위치를 바꿔줘야함
node_find = dict()

for i in range(m):
    line = list(map(int, stdin.readline().split()))
    #줄에 사람이 없는 경우
    if line[0] == 0:
        continue
    
    #1개 이상인 경우 처음은 시작 노드로 기록!
    node_find[line[1]] = Node(line[1])
    lines[i] = node_find[line[1]] #lines에 시작 노드 기록
    people_line[line[1]] = i #해당 번호의 사람이 몇번 줄에 있는 지 기록
    #시작노드인 tmp 뒤로 나머지 줄 세움
    tmp = lines[i]
    for j in range(1, line[0]): #인덱스가 같아서 문제였음! 주의!
        num = line[j+1]
        node_find[num] = Node(num)
        people_line[num] = i
        connect(tmp, node_find[num])
        tmp = tmp.next

#줄 입력 체크
# print("줄 입력 체크")
# for i in range(m):
#     tmp = lines[i]
#     while tmp != None:
#         print(tmp.data, end= " ")
#         tmp=tmp.next
#     print()
# print(people_line)
# print("\n\n\n")

for t in range(q):
    message = list(map(int, stdin.readline().split()))
    if message[0] == 1:
        a, b = node_find[message[1]], node_find[message[2]]

        #a가 맨 앞인 경우..
        if lines[people_line[message[1]]] is a: #lines[people_line[message[1]]] != -1 and 는 불가능한 경우라서 뺌
            lines[people_line[message[1]]] = a.next
        
        #b가 맨 앞인 경우
        if lines[people_line[message[2]]] is b:
            lines[people_line[message[2]]] = a

        #a의 줄정보를 b의 줄 정보로!
        people_line[message[1]] = people_line[message[2]]

        connect(a.prev, a.next) #a앞뒤를 연결
        connect(b.prev, a) #b의 앞과 a를 연결
        connect(a, b) #a와 b를 연결
    elif message[0] == 2:
        a = node_find[message[1]]

        #a가 맨 앞인 경우..
        if lines[people_line[message[1]]] is a:
            lines[people_line[message[1]]] = a.next

        people_line[message[1]] = 0

        connect(a.prev, a.next)
        a.prev = a.next = None
    elif message[0] == 3:
        a,b,c = node_find[message[1]], node_find[message[2]], node_find[message[3]]
        
        #코드 형태가 비슷해서 복붙하고 세부 값을 조정안해서 오류 발생..
        #a가 맨 앞인 경우..
        if lines[people_line[message[1]]] is a:
            lines[people_line[message[1]]] = b.next

        #c가 맨 앞인 경우
        if lines[people_line[message[3]]] is c:
            lines[people_line[message[3]]] = a

        tmp = a
        while tmp != b: #a부터 b가 되기 전까지 c로 줄정보 이동
            people_line[tmp.data] = people_line[c.data]
            tmp = tmp.next
        people_line[tmp.data] = people_line[c.data] #마지막으로 b의 줄정보 이동

        connect(a.prev, b.next) #a의 앞과 b의 뒤를 연결
        connect(c.prev, a) #c의 앞과 a를 연결
        connect(b, c) #b와 c를 연결
    else:
        print(message, "error\n\n")

    # print(message)
    # print("줄 입력 체크")
    # for i in range(m):
    #     tmp = lines[i]
    #     while tmp != None:
    #         print(tmp.data, end= " ")
    #         tmp=tmp.next
    #     print()
    # print(people_line)
    # print("\n\n\n")

for i in range(m):
    if lines[i] == None:
        print(-1)
        continue

    tmp = lines[i]
    while tmp != None:
        print(tmp.data, end= " ")
        tmp=tmp.next
    print()