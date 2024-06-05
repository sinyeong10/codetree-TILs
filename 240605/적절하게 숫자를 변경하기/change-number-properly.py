# from sys import stdin
# n, m = list(map(int, stdin.readline().split()))
# base = list(map(int, stdin.readline().split()))

# #유사도가 가장 높은 수열 : 값이 유사도
# #n이라는 길이, 1~4는 해당 숫자를 선택하는 경우, m 비슷한 수열의 제한 조건

# #dp[i][j][k] i는 비슷한 수열의 카운팅, j는 현재 인덱스, k는 1~4중 어떤 숫자인지

# dp = [[[-1]*(4) for _ in range(n)] for _ in range(m+2)]

# for k in range(4):
#     if base[0] == k+1:
#         dp[0][0][k] = 1
#     else:
#         dp[0][0][k] = 0

# # print(dp)

# #이전에서 가져오는 것은 모든[이전, 현재 의미] 비슷한 수열의 조건의 값을 가진 상태를 확인해야함!
# for i in range(m+1): #비슷한 수열이 0인 것 부터 m인 것 까지 계산
#     for j in range(1, n): #현재 보는 인덱스
#         for k in range(4):
#             tmp = 0
#             if k+1 == base[j]: #현재 들어갈 숫자가 인덱스의 숫자와 같아 유사도 1 증가!
#                 tmp = 1

#             for prev_k in range(4):
#                 if k == prev_k: #이전과 숫자가 같은 경우
#                     dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][prev_k]+tmp)
#                 else: #이전과 숫자가 달라 비슷한 수열의 카운팅횟수 1증가
#                     # print(i,j,k,prev_k, dp[i][j-1][prev_k])
#                     dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j-1][prev_k]+tmp)


#                 # #같은 비슷한 수열의 조건의 값이 불가능한 경우를 패스하는 것이 아닌
#                 # #모든 비슷한 수열의 조건의 값중 -1이 아닌 경우에 시도해야함
#                 # #이전 숫자와 같은 숫자를 선택하는 경우
#                 # if dp[i][j-1][prev_k] != -1:
#                 #     if k == prev_k: #이전과 숫자가 같은 경우
#                 #         dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][prev_k]+tmp)
#                 # #이전 숫자와 다른 숫자를 선택하는 경우
#                 # elif i != 0 and dp[i-1][j-1][prev_k] != -1:
#                 #     if k != prev_k: #이전과 숫자가 달라 비슷한 수열의 카운팅횟수 1증가
#                 #         dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j-1][prev_k]+tmp)
#                 # else:
#                 #     print(i,j,k, prev_k)
#     # print(i)
#     # print(dp)

# ans = 0
# for i in range(m+1):
#     ans = max(ans, max(dp[i][-1]))
# print(ans)

import sys

MAX_K = 4
INT_MIN = -sys.maxsize    
    
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
a = [
    0
    for _ in range(n + 1)
]

# dp[i][j] :
# 마지막으로 놓은 블록의 끝 위치가 i이고
# 지금까지 놓은 블록의 수가 j개일 때
# 얻을 수 있는 최대 유사도
dp = [
    [0 for _ in range(m + 2)]
    for _ in range(n + 1)
]


# [start_index, end_index] 구간에 전부 k로 채웠진 블록을 하나 넣었을 때
# 얻을 수 있는 유사도 값을 계산해 반환합니다.
def similarity(start_index, end_index, k):
    return sum([
        a[i] == k
        for i in range(start_index, end_index + 1)
    ])


def initialize():
    # 최댓값을 구하는 문제이므로, 
    # 초기에는 전부 INT_MIN을 넣어줍니다.
    for i in range(1, n + 1):
        for j in range(0, m + 2):
            dp[i][j] = INT_MIN
    
    # 처음에는 블록이 하나도 없기 때문에
    # 위치 0까지 고려했을 때, 0개의 블록을 놓은 상황에서
    # 초기 유사도 값은 0 입니다. 
    dp[0][0] = 0


given_seq = list(map(int, input().split()))
a[1:] = given_seq[:]

initialize()

for i in range(1, n + 1):
    # 정확히 i번째 숫자를 마지막으로
    # 그 동안 블록을 총 j개 사용했을 때
    # 얻을 수 있는 최대 유사도를 계산합니다.

    # 가장 마지막으로 놓은 블록의 위치를 [l, i]라 했을 때
    # 해당 구간에 전부 k로 채웠진 블록을 사용한 경우를 고려해봅니다.
    for j in range(1, m + 2):
        for k in range(1, MAX_K + 1):
            for l in range(1, i + 1):
                # [l, i] 구간에 전부 k로 채워진 블록을 하나 추가한 경우입니다.
                # 지금까지의 사용한 블록의 수가 j가 되기 위해서는
                # l - 1번째까지 사용한 블록의 수가 j - 1이어야 하므로
                # dp[l - 1][j - 1]에 
                # [l, i] 구간에 전부 k로 채웠진 블록을 하나 추가했을 때 
                # 얻을 수 있는 유사도를 더한 값을 비교해볼 수 있습니다.
                dp[i][j] = max(dp[i][j], dp[l - 1][j - 1] + similarity(l, i, k))

# n개의 숫자에 대해 전부 고려했을 때,
# 사용한 블록의 수가 m + 1을 넘지 않는 경우 중
# 가장 높은 유사도를 얻을 수 있는 경우를 선택합니다.

ans = max(dp[n][1:m + 2])

print(ans)