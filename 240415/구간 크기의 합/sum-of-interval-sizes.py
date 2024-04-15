from sys import stdin
n = int(stdin.readline())

point = []
for _ in range(n):
    a, b = list(map(int, stdin.readline().split()))
    point.append((a, +1))
    point.append((b, -1))

point.sort()

ans = 0
total = 0
for i in range(2*n):
    if total >= 1:
        ans += point[i][0] - point[i-1][0]
    total += point[i][1]
print(ans)