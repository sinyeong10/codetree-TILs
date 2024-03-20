from sys import stdin
n, k = list(map(int, stdin.readline().split())) #번째 단위!
switch = [list(map(int, stdin.readline().split())) for _ in range(k)]

base = list(range(n+1))

count = [{i} for i in range(n+1)]
for _ in range(3):
    for i in range(k):
        a,b = switch[i]
        base[a], base[b] = base[b], base[a]
        count[base[a]].add(a)
        count[base[b]].add(b)
        # print(base)
        # print(count)

for i in range(1, n+1):
    print(len(count[i]))