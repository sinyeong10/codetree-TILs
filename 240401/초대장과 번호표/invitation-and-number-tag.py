from sys import stdin
n, g = list(map(int, stdin.readline().split()))

# #O(ng)
# group = [set(list(map(int, stdin.readline().split()))[1:]) for _ in range(g)]
# print(group)

# ans = {1}
# for i in range(g):
#     if 1 in group[i]:
#         group[i].remove(1)

#set의 경우 add는 중복이 발생하지 않아 while 중첩 빼도 되긴함, 단 시간 더 걸림
# from collections import deque #tmp를 set이 아닌 큐로 관리
# tmp = deque()
# tmp.append(1)
# # tmp = {1}
# while tmp:
#     while tmp:
#         # key = list(tmp)[0]
#         key = tmp.popleft()
#         ans.add(key)
#         # tmp.remove(key)
#         for i in range(g):
#             if key in group[i]:
#                 group[i].remove(key)

#     for i in range(g):
#         if len(group[i]) == 1:
#             # tmp.add(list(group[i])[0])
#             tmp.append(list(group[i])[0])
#     # print(tmp)
#     # print(group)
# print(len(ans))

# #인덱스로 변환 필요!
# people_groups = [[] for _ in range(n)] #각 사람이 속하는 그룹을 의미
# visited = [False]*n #set으로 찾으면 평균적으로 O(1), 리스트의 위치로 찾아가면 O(1)
# groups = [set() for _ in range(g)]

# from collections import deque
# q = deque()
# ans = 0

# for i in range(g):
#     nums = list(map(int, stdin.readline().split()))[1:]
#     for num in nums:
#         num -= 1 #인덱스단위로 변환
#         groups[i].add(num)
#         people_groups[num].append(i)

# q.append(0)
# visited[0] = True
# while q:
#     key = q.popleft()
#     ans += 1

#     for g_num in people_groups[key]: #key가 포함된 그룹
#         groups[g_num].remove(key)
#         #삭제후 1명이면 초대장을 받음
#         if len(groups[g_num]) == 1:
#             p_num = list(groups[g_num])[0]
#             if not visited[p_num]:
#                 visited[p_num] = True
#                 q.append(p_num)

# print(ans)



people_groups = [[] for _ in range(n)] #각 사람이 속하는 그룹을 의미
groups = [set() for _ in range(g)]


for i in range(g):
    nums = list(map(int, stdin.readline().split()))[1:]
    for num in nums:
        num -= 1 #인덱스단위로 변환
        groups[i].add(num)
        people_groups[num].append(i)
# print(groups, people_groups)

visited = {0}
q = {0}

while q:
    key = list(q)[0]
    visited.add(key)
    q.remove(key)

    for g_num in people_groups[key]: #key가 포함된 그룹
        # print(g_num, key, people_groups[key])
        groups[g_num].remove(key)
        #삭제후 1명이면 초대장을 받음
        if len(groups[g_num]) == 1:
            p_num = list(groups[g_num])[0]
            if p_num not in visited:
                visited.add(p_num)
                q.add(p_num)
print(len(visited))