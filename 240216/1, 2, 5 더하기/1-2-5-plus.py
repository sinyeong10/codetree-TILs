from sys import stdin
n = int(stdin.readline())

#해당 인덱스까지 1,2,5로 나타내는 경우의 수
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 5
# dp[5] = 9

for i in range(2, n+1):
    for num in [1,2,5]:
        if i>=num:
            dp[i] += dp[i-num]
print(dp[-1])