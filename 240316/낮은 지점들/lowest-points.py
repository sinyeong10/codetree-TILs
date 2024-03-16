from sys import stdin
n = int(stdin.readline())
point = {}
for _ in range(n):
    x, y = list(map(int, stdin.readline().split()))

    if x in point:
        if point[x] > y:
            point[x] = y
    else:
        point[x] = y

total = 0
for value in point.values():
    total += value
print(total)