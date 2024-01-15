from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

dp = [0 for _ in range(m+1)]

dp[0] = 0
for i in range(1, m+1): #1~m원까지 필요한 동전의 갯수
    min_value = float("inf")
    for j in range(n):
        if i < base[j]: #금액보다 동전 가치가 크면 패스
            continue
        min_value = min(min_value, dp[i-base[j]]+1) #현재 선택한 동전의 가치 전의 합과 현재 동전을 선택
    dp[i] = min_value if min_value != float("inf") else 0 #동전을 선택 불가능한 금액이 있을 수 있음!
print(-1 if dp[m]==0 else dp[m])