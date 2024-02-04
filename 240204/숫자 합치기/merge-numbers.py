#최솟값 2개는 뽑아서 활용하고 사라지고, 더했을 때 자동으로 정렬되어야 함

from sys import stdin
n = int(stdin.readline())

# #SortedSet이용
# from sortedcontainers import SortedSet
# base = SortedSet()
# count = 0
# for elem in list(map(int, stdin.readline().split())):
#     base.add((elem, count))
#     count += 1
# total = 0
# # print(base)
# while len(base) >= 2: #2개 이상이면 계속 합침
#     a,b = base[0], base[1] #최솟값 O(1)
#     total += a[0]+b[0]
#     base.remove(a) #t삽입, 삭제 O(logn)
#     base.remove(b)
#     base.add((a[0]+b[0], count))
#     count += 1
# print(total)

#min-heap 이용
import heapq
base = list(map(int, stdin.readline().split()))
pq = []
total = 0
for elem in base:
    heapq.heappush(pq, elem)

while len(pq) >= 2: #2개 이상이면 계속 합침
    a = heapq.heappop(pq) #최솟값 O(1)
    b = heapq.heappop(pq)

    total += a+b
    heapq.heappush(pq, a+b) #삽입 O(logn)
print(total)