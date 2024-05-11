from sys import stdin
base = list(stdin.readline().strip())
n=len(base)
check = True
for i in range(n):
    if check:
        if base[i] != "1":
            base[i] = "1"
            check = False
    else:
        break

#마지막까지 0인게 없어서 처리되지 않았다면 마지막을 0으로 설정!
if check:
    base[-1] = "0"

ans = 0
cnt = 1
for i in range(n-1,-1,-1):
    ans += int(base[i])*cnt
    cnt *= 2
print(ans)