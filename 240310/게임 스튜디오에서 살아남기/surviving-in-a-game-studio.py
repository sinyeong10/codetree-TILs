from sys import stdin
n = int(stdin.readline())

dp = [[0]*4 for _ in range(n)]

total = 0
ans = []

def sol(idx, cnt):
    global total
    if idx == n:
        total += 1
        # print(ans)
        return
    
    ans.append("G")
    sol(idx+1, cnt)
    ans.pop()

    if cnt < 2: #2번까지 가능!
        ans.append("T")
        sol(idx+1, cnt+1)
        ans.pop()

    if len(ans) >= 2 and ans[-1] == "B" and ans[-2] == "B":
        return
    ans.append("B")
    sol(idx+1, cnt)
    ans.pop()

sol(0, 0)
print(total%(10**9+7))