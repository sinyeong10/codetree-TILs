from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if base[i] <= base[j] <= base[k]:
                cnt += 1
print(cnt)