from sys import stdin
n = int(stdin.readline())
lines = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
lines.sort()
print(lines)

L = [0 for _ in range(n+1)]
for i in range(n):
    L[i+1] = max(L[i], lines[i][1])

R = [10**7+1 for _ in range(n+1)]
for i in range(n-1, -1, -1):
    R[i] = min(R[i+1], lines[i][1])
print(L, R)

total = 0
for i in range(n):
    if L[i+1] == R[i]:
        total += 1
print(total)