from sys import stdin
n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
C = list(map(int, stdin.readline().split()))
D = list(map(int, stdin.readline().split()))

AB = {}
for i in range(n):
    for j in range(n):
        tmp = A[i]+B[j]
        if tmp in AB:
            AB[tmp] += 1
        else:
            AB[tmp] = 1

CD = {}
for i in range(n):
    for j in range(n):
        tmp = C[i]+D[j]
        if tmp in CD:
            CD[tmp] += 1
        else:
            CD[tmp] = 1

total = 0
for key, value in AB.items():
    if -key in CD:
        total += value*CD[-key]
print(total)