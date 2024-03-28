from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

night = {}
for i in range(n): #번호로 노드를 찾을 수 있음!
    night[base[i]] = Node(base[i])

# for elem in night:
#     print(elem.data)

for i in range(n-1):
    night[base[i]].next = night[base[i+1]]
    night[base[i+1]].prev = night[base[i]]

night[base[0]].prev = night[base[-1]]
night[base[-1]].next = night[base[0]]

for _ in range(m):
    num = int(stdin.readline())
    target = night[num]
    #시계방향에 주위, 각 target기준에서 왼쪽과 오른쪽[현재 시계방향이 next임]
    print(target.next.data, target.prev.data)
    target.prev.next, target.next.prev = target.next, target.prev

    #target의 초기화도 들어가는 게 혹시 모를 접근시 오류 방지 가능
    target.prev = target.next = None