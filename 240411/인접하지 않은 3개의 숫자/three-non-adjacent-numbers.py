from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

L = [0 for _ in range(n+1)]
for i in range(n):
    L[i+1] = max(L[i], base[i])

R = [0 for _ in range(n+1)]
for i in range(n-1,-1,-1):
    R[i] = max(R[i+1], base[i])

# print(L, base, R)

max_value = 0
for i in range(2, n-2):
    # print(i-1,i,i+2)
    max_value = max(max_value, base[i] + L[i-1]+ R[i+2])
print(max_value)