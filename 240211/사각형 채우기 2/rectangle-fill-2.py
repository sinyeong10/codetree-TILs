from sys import stdin
n = int(stdin.readline())
dp = [0 for _ in range(n+1)]

dp[0] = 1 #의미적 초기화!
dp[1] = 1

for i in range(2,n+1):
    dp[i] = (dp[i-1]%10007+dp[i-2]*2%10007)%10007
    #개별 원소 %후 마지막에도 %필요 개별원소가 더해져 넘을 수 있기 때문!
print(dp[-1])