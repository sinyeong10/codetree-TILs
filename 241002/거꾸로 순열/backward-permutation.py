from sys import stdin
n = int(stdin.readline())
visit = [False for _ in range(n+1)]
ans = []

def back_track(cnt):
    if cnt == n:
        print(*ans)
        return
    
    for i in range(n, 0, -1):
        if visit[i]:
            continue
        visit[i] = True
        ans.append(i)
        back_track(cnt+1)
        visit[i] = False
        ans.pop()

back_track(0)