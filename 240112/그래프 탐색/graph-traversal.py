from sys import stdin
n, m = list(map(int, stdin.readline().split()))
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = list(map(int, stdin.readline().split()))
    graph[s].append(e)
    graph[e].append(s)

visited = [False for _ in range(n+1)]

# def dfs(node): #현재 방문 노드!
#     total = 0 #현재 노드의 자식의 총합
#     visited[node] = True
#     # print(node)
#     for next_node in graph[node]:
#         if visited[next_node]:
#             continue
#         # print("이동", next_node)
#         total += 1 #다음 노드
#         total += dfs(next_node) #for문 돌며 자식의 경우를 다 더함
#     return total #자식 다 더한 결과를 부모에 전달
#print(dfs(1)) #여기선 처음 시작노드를 제외하고 카운트됨

def dfs(node): #현재 방문 노드!
    total = 1 #현재 노드와 자식의 총합
    visited[node] = True
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        # total += 1 #다음 노드를 여기선 체크안해도 됨!
        total += dfs(next_node) #for문 돌며 자식의 경우를 다 더함
    return total #자식 다 더한 결과를 부모에 전달

print(dfs(1)-1) #1번 노드 제외