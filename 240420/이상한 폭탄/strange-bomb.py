from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = [int(stdin.readline()) for _ in range(n)]
l_index = [-1 for _ in range(n)] #i의 왼쪽으로 가장 인접한 것!
#a,a가 있을 때 우측의 a가 터지는 지 체크만 해도 됨!
last_idx = {} #마지막 숫자의 위치
for i in range(n):
    if base[i] not in last_idx:
        l_index[i] = -1
    else:
        l_index[i] = last_idx[base[i]]
    last_idx[base[i]] = i

max_value = -1
for i in range(n):
    if l_index[i] != -1 and i-l_index[i] <= k:
        max_value = max(max_value, base[i])
print(max_value)