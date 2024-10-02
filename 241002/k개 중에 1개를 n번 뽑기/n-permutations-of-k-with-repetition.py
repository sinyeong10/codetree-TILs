from sys import stdin
k, n = list(map(int,stdin.readline().split()))
ans = []

def back_track(cnt):
    if cnt == n:
        print(*ans)
        return
    
    for i in range(1, k+1):
        ans.append(i)
        back_track(cnt+1)
        ans.pop()

back_track(0)