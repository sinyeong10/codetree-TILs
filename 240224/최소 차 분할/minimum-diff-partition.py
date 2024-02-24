from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
base.sort()
from collections import deque
A = deque()
B = deque()
total_A = 0
total_B = 0
for elem in base:
    if total_A > total_B:
        total_B+=elem
        B.append(elem)
    else:
        total_A+=elem
        A.append(elem)
# print(A,B,total_A,total_B)

standard = abs(total_A-total_B)
while True:
    if total_A-total_B < 0: #B가 더 큼
        elem = B.popleft()
        total_A += elem
        total_B -= elem
        A.append(elem)
    elif total_B-total_A < 0: #B가 더 큼
        elem = A.popleft()
        total_A -= elem
        total_B += elem
        B.append(elem)
    else:
        break
    tmp = abs(total_A-total_B)
    if tmp <= standard:
        standard = tmp
    else: #최솟값을 옮겨 tmp가 더 작아짐
        break
# print(A,B,total_A,total_B)
print(standard)