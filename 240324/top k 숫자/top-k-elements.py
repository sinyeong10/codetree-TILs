from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = set(map(int, stdin.readline().split()))
base = sorted(list(base), reverse = True)

for i in range(k):
    print(base[i], end=" ")