from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

#메모리 초과!
# count = {}
# total = 0
# for elem in base:
#     diff = k-elem
#     if diff in count:
#         total += count[diff]
    
#     tmp = []
#     for still in count.keys():
#         # print(still)
#         # if still != elem: #값이 같아도 이전에 나온 갯수만 큼 들어감!
#         # count[still+elem] = count[still] #순회하면서 수정 불가능!
#         tmp.append((still+elem, count[still]))
    
#     for idx, value in tmp:
#         count[idx] = value
    
#     if elem in count:
#         count[elem] += 1
#     else:
#         count[elem] = 1
# print(total)

total = 0
for i in range(n):
    for j in range(i):
        for q in range(j):
            if base[i]+base[j]+base[q] == k:
                total += 1
print(total)



# count = {}
# total = 0
# for i in range(n): #순차적으로 보는 기준!
#     for j in range(i): #현재 보는 값 이전의 모든 값
#         diff = k-base[i]-base[j]
#         if diff in count:
#             if diff == base[j]: #2, 3번째가 같은 경우
#                 total += count[base[j]]*(count[base[j]]-1) #2,3의 숫자가 한개인 경우는 1이 됨!
#             else:
#                 total += count[diff]*count[base[j]]
#         print(i,j,total)
#     if base[i] in count:
#         count[base[i]] += 1
#     else:
#         count[base[i]] = 1
    
# print(total//2)