from sys import stdin
k, n = list(map(int, stdin.readline().split()))
ans = []

def back_track(cnt, same_len):
    # print(cnt, same_len)
    if cnt == n:
        print(*ans)
        return

    for i in range(1, k+1):
        if same_len == 0 or (ans[-1] == i and same_len<=1):
            ans.append(i)
            back_track(cnt+1, same_len+1)
            ans.pop()
        elif ans[-1] != i:
            ans.append(i)
            back_track(cnt+1, 1)
            ans.pop()

back_track(0, 0)