from sys import stdin
n = int(stdin.readline())

dp = [0 for _ in range(n+1)]
#인덱스는 2xidx에서 idx에 해당하는 값으로 dp는 해당 사각형의 채워지는 방법의 수를 의미

dp[1] = 1
dp[2] = 2
dp[3] = 3

#세로 1개인 dp[i-1]과 가로 2개인 dp[i-2]의 경우가 dp[i]의 경우의 수
for i in range(3, n+1): #2부터 계산하고 싶다면 의미상 dp[0]=1로 해서 처리해야함
    dp[i] = dp[i-1]+dp[i-2]

# print(dp)

print(dp[-1]%10007)