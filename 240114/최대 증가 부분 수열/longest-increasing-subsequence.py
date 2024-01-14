from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

dp = [0 for _ in range(n)] #i는 i번째까지 본 것

#처음만 초기화하는 것이 아니라 이후에 처음일 수 있으므로 1부터 max_value가 시작해야 됨
# dp[0] = 1

for i in range(n):
    max_value = 1
    for j in range(i): #이전에서 가능한 값
        if base[j] < base[i]:
            max_value = max(max_value, dp[j]+1)
    dp[i] = max_value

print(max(dp))