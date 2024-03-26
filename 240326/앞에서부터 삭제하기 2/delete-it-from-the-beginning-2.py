from sys import stdin

n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

import heapq
ans = 0
total = base[-1]
hq = []
heapq.heappush(hq, base[-1])

for i in range(n-2, 0, -1):
    heapq.heappush(hq, base[i])
    total += base[i]

    #제거하지 않고 [0]가 최솟값이므로 가져와서 활용 가능!
    
    #최솟값 제거
    tmp = heapq.heappop(hq)
    total -= tmp
    # print(base[i], total, len(hq), total/len(hq))
    #평균 계산
    ans = max(ans, total/len(hq))
    #다시 복구
    heapq.heappush(hq, tmp)
    total += tmp

print(f"{ans:.2f}")