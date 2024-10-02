from sys import stdin
n = int(stdin.readline())

ans = []
visit = [False for _ in range(n)]

def back_track(cnt):
    if cnt == n:
        print(*ans)
        return

    for i in range(n): #i+1인 숫자가 들어감
        if not visit[i]:
            visit[i] = True
            ans.append(i+1)
            back_track(cnt+1)
            visit[i] = False
            ans.pop()

back_track(0)