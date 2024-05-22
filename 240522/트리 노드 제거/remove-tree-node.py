from sys import stdin
n = int(stdin.readline())
parent = list(map(int, stdin.readline().split()))
del_node = int(stdin.readline())

graph = [[] for _ in range(n)]
for i in range(n):
    if parent[i] == -1:
        root = i
        continue
    # graph[i].append(parent[i])
    graph[parent[i]].append(i) #위에서 아래로 가는 경우만 기록

# print(graph)

def count(node):
    if node == del_node:
        return 0
    tmp = 0
    for elem in graph[node]:
        tmp += count(elem)
    if not graph[node]:
        tmp += 1
    return tmp

print(count(root))