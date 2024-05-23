from sys import stdin
k, n = list(map(int, stdin.readline().split()))
ans = []

def check(i, cnt):
    # print(i, cnt)
    if cnt == n:
        print(*ans)
        return

    for j in range(1, k+1):
        ans.append(j)
        check(j, cnt+1)
        ans.pop()

check(1, 0)