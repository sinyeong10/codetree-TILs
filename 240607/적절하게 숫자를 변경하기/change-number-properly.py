# #처음 풀이, 이전 값을 통해 현재 값을 갱신
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
#                     #i,j,k시점에서 앞에선 값을 채우는 데 여기서 i+1,j,k의 값을 뿌리는 건 햇갈림..
#                     # dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j-1][prev_k]+tmp)
#                     dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][prev_k]+tmp)

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


# #두번째 풀이, 첫번째 풀이에서 불가능한 경우은 계산하지 않음!
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

# #이전에서 가져오는 것은 모든[이전, 현재 의미] 비슷한 수열의 조건의 값을 가진 상태를 확인해야함!
# for i in range(m+1): #비슷한 수열이 0인 것 부터 m인 것 까지 계산
#     for j in range(1, n): #현재 보는 인덱스
#         for k in range(4):
#             tmp = 0
#             if k+1 == base[j]: #현재 들어갈 숫자가 인덱스의 숫자와 같아 유사도 1 증가!
#                 tmp = 1

#             for prev_k in range(4):
#                 if k == prev_k and dp[i][j-1][prev_k] != -1: #이전과 숫자가 같은 경우
#                     dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][prev_k]+tmp)
#                 elif k != prev_k and dp[i-1][j-1][prev_k] != -1: #이전과 숫자가 달라 비슷한 수열의 카운팅횟수 1증가
#                     dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][prev_k]+tmp)

# ans = 0
# for i in range(m+1):
#     ans = max(ans, max(dp[i][-1]))
# print(ans)

#처음 풀이 틀린 이유 분석
from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

#유사도가 가장 높은 수열 : 값이 유사도
#n이라는 길이, 1~4는 해당 숫자를 선택하는 경우, m 비슷한 수열의 제한 조건

#dp[i][j][k] i는 비슷한 수열의 카운팅, j는 현재 인덱스, k는 1~4중 어떤 숫자인지

dp = [[[-1]*(4) for _ in range(n)] for _ in range(m+2)]

for k in range(4):
    if base[0] == k+1:
        dp[0][0][k] = 1
    else:
        dp[0][0][k] = 0

# print(dp)

#이전에서 가져오는 것은 모든[이전, 현재 의미] 비슷한 수열의 조건의 값을 가진 상태를 확인해야함!
for i in range(m+1): #비슷한 수열이 0인 것 부터 m인 것 까지 계산
    for j in range(1, n): #현재 보는 인덱스
        for k in range(4):
            tmp = 0
            if k+1 == base[j]: #현재 들어갈 숫자가 인덱스의 숫자와 같아 유사도 1 증가!
                tmp = 1

            for prev_k in range(4):
                # if k == prev_k: #이전과 숫자가 같은 경우
                #     dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][prev_k]+tmp)
                # else: #이전과 숫자가 달라 비슷한 수열의 카운팅횟수 1증가
                #     # print(i,j,k,prev_k, dp[i][j-1][prev_k])
                #     #i,j,k시점에서 앞에선 값을 채우는 데 여기서 i+1,j,k의 값을 뿌리는 건 햇갈림..
                #     # dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j-1][prev_k]+tmp)
                #     dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][prev_k]+tmp)

                #같은 비슷한 수열의 조건의 값이 불가능한 경우를 패스하는 것이 아닌
                #모든 비슷한 수열의 조건의 값중 -1이 아닌 경우에 시도해야함
                #이전 숫자와 같은 숫자를 선택하는 경우
                if dp[i][j-1][prev_k] != -1 and k == prev_k: #이전과 숫자가 같은 경우
                    # print("이전과 숫자가 같은 경우\n", i,j,k, prev_k, " : ", dp[i][j-1][prev_k])
                    # print(dp[i][j][k],"에 이 값을 갱신 시도", dp[i][j-1][prev_k]+tmp)
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][prev_k]+tmp)
                #이전 숫자와 다른 숫자를 선택하는 경우
                elif dp[i][j-1][prev_k] != -1 and k != prev_k: #이전과 숫자가 달라 비슷한 수열의 카운팅횟수 1증가
                    # print("이전과 숫자가 다른 경우\n", i,j,k, prev_k, " : ", dp[i][j-1][prev_k])
                    # print(dp[i+1][j][k],"에 이 값을 갱신 시도", dp[i][j-1][prev_k]+tmp)
                    dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j-1][prev_k]+tmp)
                # elif i != 0:
                #     print(i,j,k, prev_k, " : ", dp[i][j-1][prev_k])
    # print(i)
    # print(dp)

ans = 0
for i in range(m+1):
    ans = max(ans, max(dp[i][-1]))
print(ans)