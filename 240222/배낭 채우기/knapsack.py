from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]
# base.sort(key = lambda x : (-x[1]/x[0], x[0])) #w:v=1:? => v/w
# print(base)

dp = [-1]*(m+1) #무게가 key일 때 가치가 value
dp[0] = 0

for w, v in base:
    for j in range(m,-1,-1):
        if dp[j] != -1 and j+w <=m:
            dp[j+w] = max(dp[j+w], dp[j]+v)
print(max(dp))