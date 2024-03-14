from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

#2가지 덧셈의 결과를 다 저장 : 메모리 초과! #모두 1인 경우 틀림..
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
# print(count)

#완전 탐색 : 시간초과 나올 수 있음!
# total = 0
# for i in range(n):
#     for j in range(i):
#         for q in range(j):
#             if base[i]+base[j]+base[q] == k:
#                 total += 1
# print(total)



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



arr = base

count = dict()

# 각 숫자가 몇 번씩 나왔는지를
# hashmap에 기록해줍니다.
for elem in arr:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

ans = 0
# 배열을 앞에서부터 순회하며 쌍을 만들어줍니다.
for i in range(n):
    # 이미 순회한 적이 있는 숫자는 빼 버림으로서
    # 같은 조합이 여러번 세어지는 걸 방지합니다.
    count[arr[i]] -= 1

    for j in range(i):
        # 전처리를 해주었기 때문에 이미 순회한 적 있는 값은 hashmap에 없습니다.
        # 이와 같은 방식으로 같은 조합이 중복되어 세어지는 걸 방지할 수 있습니다.
        diff = k - arr[i] - arr[j]

        if diff in count:
            ans += count[diff]

print(ans)