from sys import stdin
n, m, k = list(map(int, stdin.readline().split()))
base = [stdin.readline().strip() for _ in range(n)]

a = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        value = 1 if base[i][j] == "a" else 0
        a[i+1][j+1] = a[i+1][j]+a[i][j+1]-a[i][j]+value

# for elem in a:
#     print(*elem)

b = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        value = 1 if base[i][j] == "b" else 0
        b[i+1][j+1] = b[i+1][j]+b[i][j+1]-b[i][j]+value

c = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        value = 1 if base[i][j] == "c" else 0
        c[i+1][j+1] = c[i+1][j]+c[i][j+1]-c[i][j]+value

for _ in range(k):
    r1, c1, r2, c2 = list(map(int, stdin.readline().split()))
    r1, c1 = r1-1, c1-1
    print(a[r2][c2]-a[r2][c1]-a[r1][c2]+a[r1][c1],\
     b[r2][c2]-b[r2][c1]-b[r1][c2]+b[r1][c1], \
     c[r2][c2]-c[r2][c1]-c[r1][c2]+c[r1][c1])