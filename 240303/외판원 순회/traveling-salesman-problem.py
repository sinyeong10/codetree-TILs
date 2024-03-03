from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

visited = [False]*n

#처음 출발지는 1번지점으로 고정!
visited[0] = True
ans = [0]

import sys
def sol(cnt):
    cost = sys.maxsize
    if cnt == n:
        tmp = 0
        for i in range(n-1):
            tmp+=base_2d[ans[i]][ans[i+1]]
        tmp+=base_2d[ans[-1]][0]
        # print(ans, tmp)
        return tmp
    
    for i in range(n):
        if visited[i]: #이전에 간 경우는 패스
            continue
        if base_2d[ans[-1]][i] != 0: #갈 수 있으면 감
            visited[i] = True
            ans.append(i)
            cost = min(cost, sol(cnt+1))
            visited[i]=False
            ans.pop()
    return cost
print(sol(1))