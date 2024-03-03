from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [False for _ in range(n)]

ans = []
def sol(cnt): #현재 cnt개 고름
    tmp = 0
    if cnt == n:
        for q in range(n):
            x,y = ans[q]
            tmp += base_2d[x][y]
            # print(q,x,y,tmp, base_2d[x][y])
        # print(ans, tmp)
        return tmp
    
    for j in range(n): #열이 정해지면 cnt행에서 반드시 하나를 골라야함!
        if visited[j]:
            continue
        ans.append((cnt, j))
        visited[j] = True
        tmp = max(tmp, sol(cnt+1))
        ans.pop()
        visited[j] = False
    return tmp

print(sol(0))