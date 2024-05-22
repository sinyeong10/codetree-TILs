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
    if node == del_node: #시작이 삭제되는 경우는 0
        return 0
    tmp = 0
    for elem in graph[node]:
        if elem == del_node: #요소 중 삭제된 건 건너뜀
            continue
        tmp += count(elem) #가능한 건 리프 숫자 세기 시작
    if not graph[node] or graph[node] == [del_node]: #리프이거나, 아래 노드가 유일하며 삭제노드라면 카운트
        tmp += 1
    # print(node, tmp)
    return tmp

print(count(root))