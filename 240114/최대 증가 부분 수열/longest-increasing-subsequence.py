from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

dp = [0 for _ in range(n)] #i는 i번째까지 본 것

dp[0] = 1

for i in range(1, n):
    max_value = 0
    for j in range(i): #이전에서 가능한 값
        if base[j] < base[i]:
            max_value = max(max_value, dp[j]+1)
    dp[i] = max_value
    
print(max(dp))