from sys import stdin
n, m = list(map(int, stdin.readline().split()))
numbers = list(map(int, stdin.readline().split()))
ans = -float("inf")
pick_num = []

def back_track(cnt, last_idx):
    global ans
    if cnt == m:
        tmp = pick_num[0]
        for i in range(1, m):
            tmp ^= pick_num[i]
        ans = max(ans, tmp)
        return
    for i in range(last_idx+1, n):
        pick_num.append(numbers[i])
        back_track(cnt+1, i)
        pick_num.pop()

back_track(0, -1)
print(ans)