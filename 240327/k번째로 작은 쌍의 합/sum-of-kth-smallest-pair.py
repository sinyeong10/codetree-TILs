from sys import stdin
n, m, k = list(map(int, stdin.readline().split()))
first = sorted(list(map(int, stdin.readline().split())))
second = sorted(list(map(int, stdin.readline().split())))

#메모리 초과
# total = []
# for i in range(n):
#     for j in range(m):
#         total.append((first[i], second[j]))

# total.sort(key=lambda x:(x[0]+x[1]))
# a,b=total[k-1]
# print(a+b)


# find_index= {}
# for i in range(n):
#     find_index[first[i]] = i

# import heapq
# hq = []

# for j in range(m):
#     heapq.heappush(hq, (first[0]+second[j], first[0], second[j]))

# for _ in range(k):
#     ans, key, tmp = heapq.heappop(hq)
#     idx = find_index[key]
#     if idx != n-1: #마지막이 아니면 다음으로 가서 삽입
#         heapq.heappush(hq, (first[idx+1]+tmp, first[idx+1], tmp))
#     # print(key,tmp, hq)
# print(ans)
    
#굳이 위쳐럼 값을 인덱스로 변환안해도 됨, 정렬은 첫번째 값이므로 인덱스로 관리!
import heapq
hq = []

for j in range(m):
    heapq.heappush(hq, (first[0]+second[j], 0, j))

for _ in range(k):
    ans, idx1, idx2 = heapq.heappop(hq)
    if idx1 != n-1: #마지막이 아니면 다음으로 가서 삽입
        heapq.heappush(hq, (first[idx1+1]+second[idx2], idx1+1, idx2))
print(ans)