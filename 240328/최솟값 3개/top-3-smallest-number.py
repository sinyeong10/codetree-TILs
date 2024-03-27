from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
import heapq
hq = []

#간단히
# for elem in base:
#     heapq.heappush(hq, elem)
#     if len(hq) < 3:
#         print(-1)
#     else:      
#         a = heapq.heappop(hq)
#         b = heapq.heappop(hq)
#         c = heapq.heappop(hq)
#         print(a*b*c)
#         heapq.heappush(hq, a)
#         heapq.heappush(hq, b)
#         heapq.heappush(hq, c)

#최대힙으로 가장 작은 3개만 관리!
for elem in base:
    if len(hq) < 3: #3개 전은 그냥 넣기
        heapq.heappush(hq, -elem)
    else:
        tmp = -heapq.heappop(hq) #최댓값 가져와
        heapq.heappush(hq, -min(tmp, elem)) #가장 작은 걸 넣음
    
    if len(hq) == 3:
        print(-hq[0]*hq[1]*hq[2]) #-1의 3번은 -1임
    else:
        print(-1)