from sys import stdin
n = int(stdin.readline())
point = []
for _ in range(n):
    x1, x2 = list(map(int, stdin.readline().split())) #[,)으로 접근!
    point.append((x1, +1))
    point.append((x2, -1))
point.sort()

total = 0
max_value = 0
for i in range(2*n):
    total += point[i][1]
    max_value = max(max_value, total)
    # print(total)
print(max_value)