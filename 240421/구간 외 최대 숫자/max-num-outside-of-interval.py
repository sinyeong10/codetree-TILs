from sys import stdin
n, q = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

L = [0 for _ in range(n+1)]
R = [0 for _ in range(n+1)]
for i in range(n):
    L[i+1] = max(L[i], base[i])
for i in range(n-1,-1,-1):
    R[i] = max(R[i+1], base[i])
# print(L,R)
for _ in range(q):
    a, b = list(map(int, stdin.readline().split()))
    # print(L[a-1], R[b])
    print(max(L[a-1], R[b]))