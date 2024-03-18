from sys import stdin
n= int(stdin.readline())
base = list(map(int, stdin.readline().split()))

check = {}
for i in range(n):
    if base[i] not in check:
        check[base[i]] = i+1

for key, value in sorted(check.items()):
    print(key, value)