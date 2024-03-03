from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [False for _ in range(n)]

ans = []
def sol(cnt):
    tmp = 0
    if cnt == n:
        for q in range(n):
            x,y = ans[q]
            tmp += base_2d[x][y]
            # print(q,x,y,tmp, base_2d[x][y])
        # print(ans, tmp)
        return tmp
    
    for j in range(n):
        if visited[j]:
            continue
        ans.append((cnt, j))
        visited[j] = True
        tmp = max(tmp, sol(cnt+1))
        ans.pop()
        visited[j] = False
    return tmp

print(sol(0))