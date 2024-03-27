from sys import stdin
n, m, k = list(map(int, stdin.readline().split()))
first = list(map(int, stdin.readline().split()))
second = list(map(int, stdin.readline().split()))

total = []
for i in range(n):
    for j in range(m):
        total.append((first[i], second[j]))

total.sort(key=lambda x:(x[0]+x[1]))
a,b=total[k-1]
print(a+b)