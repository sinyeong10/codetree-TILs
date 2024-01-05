class Stack:
    def __init__(self):
        self.items = []

    def push(self, A):
        self.items.append(A)

    def pop(self):
        if self.empty():
            raise 
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return not self.items #없으면 True, 있으면 False

    def top(self):
        if self.empty():
            raise 
        return self.items[-1]


from sys import stdin
n = int(stdin.readline())
order = [stdin.readline().split() for _ in range(n)]

base = Stack()
for q in order:
    if q[0] == "push":
        base.push(q[1])
    elif q[0] == "pop":
        print(base.pop())
    elif q[0] == "size":
        print(base.size())
    elif q[0] == "empty":
        print(1 if base.empty() else 0)
    elif q[0] == "top":
        print(base.top())