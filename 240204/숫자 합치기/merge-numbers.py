from sys import stdin
n = int(stdin.readline())

from sortedcontainers import SortedSet
base = SortedSet()
count = 0
for elem in list(map(int, stdin.readline().split())):
    base.add((elem, count))
    count += 1

total = 0
# print(base)

while len(base) >= 2:
    a,b = base[0], base[1]
    total += a[0]+b[0]
    base.remove(a)
    base.remove(b)
    base.add((a[0]+b[0], count))
    count += 1
print(total)