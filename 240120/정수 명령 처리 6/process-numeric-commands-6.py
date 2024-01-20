import heapq

class PriorityQueue:
    def __init__(self):
        self.items=[]
    
    def push(self, A):
        heapq.heappush(self.items, -A)
    
    def pop(self):
        if self.empty():
            raise Exception("empty")
        return -heapq.heappop(self.items)

    def size(self):
        return len(self.items)
    
    def empty(self):
        return not self.items
    
    def top(self):
        if self.empty():
            raise Exception("empty")
        return -self.items[0]

from sys import stdin
n = int(stdin.readline())
base = PriorityQueue()
for _ in range(n):
    order = stdin.readline().split()
    if order[0] == "push":
        base.push(int(order[1]))
    elif order[0] =="pop":
        print(base.pop())
    elif order[0] =="size":
        print(base.size())
    elif order[0] =="empty":
        print(1 if base.empty() else 0)
    elif order[0] =="top":
        print(base.top())