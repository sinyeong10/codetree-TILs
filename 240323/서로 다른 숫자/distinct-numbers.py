from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
num = set()
for i in range(n):
    num.add(base[i])
print(len(num))