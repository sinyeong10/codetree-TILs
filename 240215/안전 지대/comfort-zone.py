from sys import stdin
import sys
sys.setrecursionlimit(10000) #재귀함수의 깊이 설정
n, m = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]


def sol(k):
    dx, dy = [-1,1,0,0], [0,0,-1,1]

    visited = [[False]*m for _ in range(n)] #방문여부
    total = 0

    def can_go(i,j):
        if not(0<=i<n and 0<=j<m): #범위 밖
            return False
        if visited[i][j] or base_2d[i][j] <= k: #방문했음, k로 인해 잠김
            return False
        return True

    def dfs(i,j):
        # print(i,j)
        visited[i][j] = True
        for dxs, dys in zip(dx, dy):
            next_i, next_j = i+dxs, j+dys
            if can_go(next_i, next_j):
                dfs(next_i, next_j)
        return 1

    for i in range(n):
        for j in range(m):
            if base_2d[i][j] > k and not visited[i][j]:
                total += dfs(i,j)
    return total

#수위가 0일때는 1임
#수위가 1일때는 0
max_value = 0 #안전영역의 수
answer = 1 #그때의 수위
for i in range(1, 100):
    tmp = sol(i)
    #가장 처음 갱신된 것이 k가 가장 작은 최대
    if max_value < tmp:
        max_value = tmp
        answer = i

    if tmp == 0: #다 잠겨서 더 안봐도 됨
        break
print(answer, max_value) #수위, 안전영역의 갯수