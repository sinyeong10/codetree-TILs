from sys import stdin
n,t = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(2)]

for _ in range(t):
    f_tmp = base[0][n-1]
    for i in range(n-1,0,-1): #n-1~...1
        base[0][i] = base[0][i-1]
    # print(base)
    l_tmp = base[1][n-1]
    for i in range(n-1,0,-1):
        base[1][i] = base[1][i-1]
    # print(base)
    base[0][0] = l_tmp
    base[1][0] = f_tmp
    # print(base)
for elem in base:
    print(*elem)