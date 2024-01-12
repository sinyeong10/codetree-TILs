from sys import stdin
n, m = list(map(int, stdin.readline().split()))
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = list(map(int, stdin.readline().split()))
    graph[s].append(e)
    graph[e].append(s)

visited = [False for _ in range(n+1)]

def dfs(node): #현재 방문 노드!
    visited[node] = True
    # print(node)
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        # print("이동", next_node)
        return dfs(next_node)+1
    return 1

print(dfs(1)-1)