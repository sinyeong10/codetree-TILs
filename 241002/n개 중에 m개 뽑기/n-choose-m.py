from sys import stdin
n, m = list(map(int, stdin.readline().split()))
ans = []

def back_track(cnt, last_num):
    if cnt == m:
        print(*ans)
    
    for num in range(last_num+1, n+1):
        ans.append(num)
        back_track(cnt+1, num)
        ans.pop()

back_track(0, 0)