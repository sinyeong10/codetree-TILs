# from sys import stdin
# n, m = list(map(int, stdin.readline().split()))
# base = list(map(int, stdin.readline().split()))

# dp = [-1 for _ in range(m+1)]

# dp[0] = 0
# for i in range(1, m+1): #1~m원까지 필요한 동전의 갯수
#     min_value = float("inf")
#     for j in range(n):
#         if i < base[j] or dp[i-base[j]] == -1: #금액보다 동전 가치가 크면 패스, 불가능도 패스
#             continue
#         min_value = min(min_value, dp[i-base[j]]+1) #현재 선택한 동전의 가치 전의 합과 현재 동전을 선택
#     dp[i] = min_value if min_value != float("inf") else -1 #동전을 선택 불가능한 금액이 있을 수 있음!
#     # print(i, dp)
# print(dp[m])

from sys import stdin
n, m = list(map(int, stdin.readline().split()))
coin = list(map(int, stdin.readline().split()))
dp = [float("inf")]*(m+1) #0~m까지 동전의 갯수, 초기값을 불가능한 값으로!
#처음
dp[0] = 0

for i in range(m+1):
    for j in range(n): #코인들 확인
        if i >= coin[j]: #금액이 코인가치보다 큰 경우만 확인
            dp[i] = min(dp[i], dp[i-coin[j]]+1) #inf와 inf+1을 처리하면 inf나옴

print(dp[m] if dp[m] != float("inf") else -1)