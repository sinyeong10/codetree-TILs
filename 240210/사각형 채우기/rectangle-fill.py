from sys import stdin
n = int(stdin.readline())

dp = [0 for _ in range(n+1)]
#인덱스는 2xidx에서 idx에 해당하는 값으로 dp는 해당 사각형의 채워지는 방법의 수를 의미

dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]

# print(dp)

print(dp[-1]%10007)