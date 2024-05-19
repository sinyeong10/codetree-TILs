from sys import stdin
n = int(stdin.readline())
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

diff = [0 for _ in range(n)]
for i in range(1, n):
    a,b = base[i]
    c,d = base[i-1]
    diff[i] = abs(a-c)+abs(b-d)
# print(diff)

L = [0 for _ in range(n)]
R = [0 for _ in range(n)]

for i in range(1, n):
    L[i] = L[i-1]+diff[i]
# print(L)

for i in range(n-2,-1,-1):
    R[i] = R[i+1]+diff[i+1]
# print(R)

import sys
ans = sys.maxsize

for i in range(1, n-1):
    a,b = base[i-1]
    c,d = base[i+1]
    ans = min(ans, L[i-1]+R[i+1]+abs(a-c)+abs(b-d))
    # print(L[i-1],R[i+1],abs(a-c)+abs(b-d))
print(ans)