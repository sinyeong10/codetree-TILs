from sys import stdin
n = int(stdin.readline())
points = []
for _ in range(n):
    a, b = list(map(int, stdin.readline().split()))
    points.append((a, +1))
    points.append((b, -1))
points.sort()

total = 0
current = 0
for elem, value in points:
    current+=value
    total = max(total, current)
print(total)