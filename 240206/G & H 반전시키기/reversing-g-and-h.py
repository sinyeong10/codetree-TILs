from sys import stdin
n = int(stdin.readline())
base = stdin.readline().strip()
target = stdin.readline().strip()
trans = [0 for _ in range(n)]

for i in range(n):
    if base[i] != target[i]:
        trans[i] += 1

# print(trans)

total = 0
idx = 0
for i in range(n):
    if trans[i] == 1 and trans[i] != idx:
        total += 1
    idx = trans[i]
print(total)