from sys import stdin
n = int(stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1): #2~n줄까지 n-1개를 체크
    a, b = list(map(int, stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

parent = [-1 for _ in range(n+1)]
parent[1] = 0

def dfs(node):
    for elem in graph[node]:
        if parent[elem] == -1:
            parent[elem] = node

            dfs(elem)

dfs(1)

for elem in parent[2:]:
    print(elem)