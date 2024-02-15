from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

max_value = 0
for i in range(n): #i 기준으로 꺽임!
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for q in range(1, n):
        for j in range(i):
            if base[q] > base[j]:
                dp[q] = max(dp[q], dp[j]+1)
        for k in range(i, n):
            if base[q] < base[k]:
                dp[q] = max(dp[q], dp[k]+1)
    # print(i, dp)
    max_value = max(max_value, max(dp))
print(max_value)