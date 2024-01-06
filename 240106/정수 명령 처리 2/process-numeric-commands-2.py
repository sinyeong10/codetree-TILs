# from collections import deque

# class Queue:
#     def __init__(self):
#         self.base = deque()
    
#     def push(self, A):
#         self.base.append(A)
    
#     def empty(self):
#         return not self.base
    
#     def size(self):
#         return len(self.base)
    
#     def pop(self):
#         if self.empty():
#             raise Exception("empty")
#         return self.base.popleft()
    
#     def front(self):
#         if self.empty():
#             raise Exception("empty")
#         return self.base[0]
    

# from sys import stdin
# n = int(stdin.readline())
# base = Queue()
# for _ in range(n):
#     order = stdin.readline().split()
#     # print(order)
#     if order[0] == "push":
#         base.push(order[1])
#     elif order[0] == "front":
#         print(base.front())
#     elif order[0] == "size":
#         print(base.size())
#     elif order[0] == "pop":
#         print(base.pop())
#     elif order[0] == "empty":
#         print(1 if base.empty() else 0)

from collections import deque

from sys import stdin
n = int(stdin.readline())
base = deque()
for _ in range(n):
    order = stdin.readline().split()
    if order[0] == "push":
        base.append(order[1])
    elif order[0] == "front":
        print(base[0])
    elif order[0] == "size":
        print(len(base))
    elif order[0] == "pop":
        print(base.popleft())
    elif order[0] == "empty":
        print(1 if not base else 0)