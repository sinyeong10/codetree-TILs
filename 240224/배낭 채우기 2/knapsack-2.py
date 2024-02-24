from sys import stdin
n, m = list(map(int, stdin.readline().split()))
jewelry = [list(map(int, stdin.readline().split())) for _ in range(n)]
# jewelry.sort() #작은 순서로 정렬하나 하지 않나 동일 #a+b와 b+a는 동일!

dp = [-1]*(m+1)
dp[0] = 0

for w, v in jewelry: #순차적으로 보석 보는중
    for j in range(1, m+1):
        if j >= w and dp[j-w] != -1: #i번째 보석의 무게
            dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])