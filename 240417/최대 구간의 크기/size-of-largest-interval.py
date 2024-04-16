from sys import stdin
n = int(stdin.readline())

point = []

for _ in range(n):
    a,b = list(map(int, stdin.readline().split()))
    point.append((a, +1))
    point.append((b, -1))

point.sort()

max_value = 0
total = 0
last = -1

for i in range(2*n):
    if total == 1 and point[i][1] == -1: #0이 되는 시점!
        max_value = max(max_value, point[i][0]-last)
        last = point[i][0]
    elif total ==0 and point[i][1] == 1: #처음 1이 되는 시점!
        last = point[i][0]
    total += point[i][1]
print(max_value)