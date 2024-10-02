from sys import stdin
n, m = list(map(int, stdin.readline().split()))
graph_node = [list(map(int, stdin.readline().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
for x, y in graph_node:
    graph[x].append(y)
    graph[y].append(x)
# print(graph)
visit = [False for _ in range(n+1)]

ans = 0
def dfs(node):
    global ans
    for next_node in graph[node]:
        if visit[next_node]:
            continue
        visit[next_node] = True    
        ans += 1
        dfs(next_node)

dfs(1)
print(ans-1)