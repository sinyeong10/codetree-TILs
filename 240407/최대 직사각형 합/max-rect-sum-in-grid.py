from sys import stdin
n = int(stdin.readline())
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

# print(base)

prefix = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        prefix[i+1][j+1] = prefix[i+1][j]+prefix[i][j+1]-prefix[i][j]+base[i][j]

# print(prefix)

max_value = -sys.maxsize
for i in range(n+1):
    for j in range(n+1):

        for q in range(i):
            for w in range(j):
                #q~i, w~j범위의 직사각형
                max_value = max(max_value, prefix[i][j]-prefix[i][w]-prefix[q][j]+prefix[q][w])
print(max_value)