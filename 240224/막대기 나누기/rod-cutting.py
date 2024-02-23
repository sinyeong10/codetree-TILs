from sys import stdin
n = int(stdin.readline())
line = list(map(int, stdin.readline().split()))

#일정 범위를 토막내어 파는 데 길이에 따라 가치가 다름!
dp = [-1]*(n+1)
dp[0] = 0
for length in range(n):
    for i in range(n):
        if i+1-length-1 >= 0 and dp[i+1-length-1] != -1:
            dp[i+1] = max(dp[i+1], dp[i+1-length-1]+line[length])
        dp[i+1] = max(dp[i+1], line[i])
print(dp[-1])