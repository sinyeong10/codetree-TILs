from sys import stdin
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

num = set()
for i in range(n):
    num.add(a[i])

for j in range(m):
    if b[j] in num:
        print(1)
    else:
        print(0)