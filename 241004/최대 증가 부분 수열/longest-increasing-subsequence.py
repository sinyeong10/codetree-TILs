from sys import stdin
n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))

dp = [1 for _ in range(n)]
# dp[0] = 1 #처음을 반드시 선택하지 않아도 됨

for i in range(n): #dp[i] : i번째까지 왔을때 가장 긴 수열
    for j in range(i):
        if numbers[j] < numbers[i]: #무조건 증가해야함
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))