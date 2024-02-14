from sys import stdin
n = int(stdin.readline())
lines = []
for _ in range(n):
    lines.append(list(map(int, stdin.readline().split())))
lines.sort(key = lambda x : (x[1], x[0]))
# print(lines)

last = -1
total = 0
for x1, x2 in lines:
    if x1 > last:
        last = x2
        total += 1
print(total)