from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

import sys
initial = -100#sys.maxsize
dp = [[initial]*(k+1) for _ in range(n)] #i번째까지 봄, j개의 음수
#k에서 아래 방향 계산만 필요한 데 범위 게산을 하지 않기 위해서 k+1까지 인덱스 생성!

#처음 초기화
dp[0][0] = base[0] if base[0] >= 0 else initial
dp[0][1] = base[0] if base[0] < 0 else initial

# for i in range(1, n):
#     if base[i] >= 0: #양수면 누적해서 더함
#         # if dp[i-1][0] != initial: #이전이 계산 가능시 누적
#         #     dp[i][0] = dp[i-1][0] + base[i]
#         # else: #이전이 불가능시 새로!
#         #     dp[i][0] = base[i]
#         #이전의 값이 없으면 -라 base[i]가 무조건 더 큼
#         dp[i][0] = max(dp[i-1][0]+base[i], base[i])

# for i in range(1, n):
#     for j in range(1, k+1):
#         #이전의 계산된 누적과, 현재 위치부터 시작하는 경우의 값
#         if base[i] < 0:
#             dp[i][j] = max(dp[i-1][j-1]+base[i], base[i])
#         else:
#             dp[i][j] = max(dp[i-1][j]+base[i], base[i])

# #위의 2개의 for문을 합칠 수 있음
# for i in range(1, n):
#     if base[i] >= 0:
#         for j in range(k+1): #처음 초기화하는 0의 경우가 안에 들어가서 처리됨!
#             dp[i][j] = max(dp[i-1][j]+base[i], base[i])
#     else:
#         for j in range(1, k+1):
#             dp[i][j] = max(dp[i-1][j-1]+base[i], base[i])



#근데 위의 for문은 의미상 음수의 갯수가 맞지 않음... 새로 갱신하는 경우가 더 좋아져도 음수의 갯수는 그대로....
for i in range(1, n):
    #처음은 이전이 없으면 현재로 생성!
    if base[i] >= 0:
        dp[i][0] =  max(dp[i-1][0]+base[i], base[i])
        for j in range(1, k+1): #처음 초기화하는 0의 경우가 안에 들어가서 처리됨!
            if dp[i-1][j] != initial:
                dp[i][j] = max(dp[i-1][j]+base[i], dp[i][j])
    else:
        dp[i][1] = max(dp[i-1][0]+base[i], base[i])
        for j in range(2, k+1):
            if dp[i-1][j-1] != initial:
                dp[i][j] = max(dp[i-1][j-1]+base[i], dp[i][j])

# for elem in dp:
#     print(*elem)

max_value = 0
for i in range(n):
    for j in range(k+1):
        max_value = max(max_value, dp[i][j])
print(max_value)