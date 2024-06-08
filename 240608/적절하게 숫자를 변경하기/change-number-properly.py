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

###

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

###

#처음 풀이 틀린 이유 분석 중
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
                # else:
                #     print(i,j,k, prev_k, " : ", dp[i][j-1][prev_k])
        # print(i, j)
        # print(dp)

ans = 0
for i in range(m+1):
    ans = max(ans, max(dp[i][-1]))
print(ans)

###

# #뿌리는 형태로 문제 풀기
# from sys import stdin
# n, m = list(map(int, stdin.readline().split()))
# base = list(map(int, stdin.readline().split()))

# #dp[i][j][k]에서 i는 비슷한 수열(m)과 관련된 값, j는 현재까지 살펴본 인덱스, k는 마지막으로 선택한 숫자
# dp = [[[-1]*4 for _ in range(n)] for _ in range(m+1)]
# # print(dp)

# for k in range(4):
#     if base[0] == k+1:
#         dp[0][0][k] = 1
#     else:
#         dp[0][0][k] = 0

# # print(dp)

# for i in range(m+1):
#     for j in range(n-1):
        
#         for k in range(4): #이게 먼저 나오면 i,j,k 기준으로 가능한 4가지 경우를 뿌림, 불가능한 값만 처리 가능!
#             if dp[i][j][k] != -1:
#                 for next_k in range(4): #이게 먼저 나오면 next_k 위치를 채우기 위해서 i,j,k의 4가지 경우를 살펴봄!, tmp를 한번만 계산가능!
#                     tmp = 1 if next_k+1 == base[j+1] else 0

#                     if k == next_k:
#                         dp[i][j+1][next_k] = max(dp[i][j+1][k], dp[i][j][k]+tmp)
#                     else:
#                         if i == m: #m인 경우 다른 숫자로 변경해서 불가능!
#                             continue
#                         dp[i+1][j+1][next_k] = max(dp[i+1][j+1][next_k], dp[i][j][k]+tmp)
#                 # print(i, j, k)
#                 # print(dp)

# ans = 0
# for i in range(m+1):
#     ans = max(ans, max(dp[i][-1]))
# print(ans)

###

# #문제의 본질을 통해 풀기
# from sys import stdin
# n, m = list(map(int, stdin.readline().split()))
# base = list(map(int, stdin.readline().split()))

# #dp[i][j]에서 i는 마지막으로 놓은 블록의 위치, j는 지금까지 놓은 블록의 수 (서로 다른 게 m개 가능하므로 총 m+1개 가능!)
# dp = [[-1 for _ in range(m+2)] for _ in range(n+1)]
# #마지막에 여유 공간을 1씩 증가시켜두면
# #j의 경우 +1이 DP식으로 들어갈 때 if문으로 마지막 경우를 처리하지 않아도 괜찮음
# #i의 경우 처음 경우를 미리 생각해서 처리하지 않아도 됨

# dp[0][0] = 0
# #위치가 없고 블록이 없으므로 0임!
# # print(dp)

# for i in range(1, n+1):
#     #i번째 위치를 마지막으로 블록을 j개 사용하는 경우를 계산
   
#     for j in range(1, m+2): #사용한 블록의 수
#         for k in range(4):
#             #[l,i]가 마지막 블록의 위치일 때 이 값을 가능한 숫자 k로 채우는 경우 중 최대
#             tmp = 0
#             #모든 가능한 l범위에 대해서 유사도를 계산
#             for l in range(i, 0, -1): #i ~ 1
#                 #역순으로 하면 매번 계산하는 것이 아닌 이전 계산 값에 현재 상태의 값을 가산하기만 하면 됨!
#                 tmp += 1 if base[l-1] == k+1 else 0 #인덱스로 변환하여 계산
#                 #i가 아닌 l의 값을 보고 처리해야함! 여기서 틀렸음!

#                 if dp[l-1][j-1] != -1: #-1이 아니라 -inf로 초기화했으면 max값을 기록하기 때문에 if문을 생략가능
#                     dp[i][j] = max(dp[i][j], dp[l-1][j-1]+tmp)
#     # print(i)
#     # print(dp)

# print(max(dp[n][1:m+2])) #n개를 다 봤고 블록의 갯수가 1~m+1개인 것 중 가장 큰 값!