from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = [[0]*(n+1)]
for _ in range(n):
    base.append([0]+list(map(int, stdin.readline().split())))
print(base)

# prefix_sum = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + \
                            prefix_sum[i][j - 1] - \
                            prefix_sum[i - 1][j - 1] + \
                            base[i][j]

# print(prefix_sum)

max_value = 0
for i in range(1, n+1-k +1): #1~n+1을 활용, 그중 k개 사용 예정, n+1-k에 +k-1시 n+1이 나오면 됨
    for j in range(1, n+1-k +1):
        a,b,c,d = i-1,j-1, i+k-1,j+k-1
        max_value = max(max_value, prefix_sum[c][d] - prefix_sum[a][d] - prefix_sum[c][b] + prefix_sum[a][b])
print(max_value)