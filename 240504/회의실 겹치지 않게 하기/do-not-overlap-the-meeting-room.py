from sys import stdin
n = int(stdin.readline())
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

base.sort(key=lambda x : (x[1],x[0]))
# print(base)

#특정 시간을 종료시점으로 잡았을 때 그때까지 가장 많은 회의를 하는 경우
ans = 0
last = -1
for i in range(n):
    a,b = base[i]
    if last <= a:
        ans += 1
        last = b
print(n-ans)