from sys import stdin
n = int(stdin.readline())

guest = []
for i in range(n):
    s,e = list(map(int, stdin.readline().split()))
    guest.append((s-1, +1))
    guest.append((e, -1)) #다음에 나감! #(a, -1)이 (a,+1)보다 먼저 나옴!

guest.sort()

total = 0
max_value = 0
for i in range(2*n):
    total += guest[i][1]
    max_value = max(max_value, total)
print(max_value)