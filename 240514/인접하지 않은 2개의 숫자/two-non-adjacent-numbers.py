from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
ans = 0
for i in range(n):
    for j in range(i+2, n):
        ans = max(ans, base[i]+base[j])
print(ans)