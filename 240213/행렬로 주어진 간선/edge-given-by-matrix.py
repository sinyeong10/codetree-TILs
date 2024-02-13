from sys import stdin
n = int(stdin.readline())

#인덱스 기준!
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(n):
    graph[i][i] = 1

for k in range(n): #가장 외곽부터 안으로 들어오며 계산됨! #거쳐가는 노드!
    for i in range(n): #시작
        for j in range(n): #끝
            if graph[i][k] * graph[k][j] == 1:
                graph[i][j] = 1

for elem in graph:
    print(*elem)