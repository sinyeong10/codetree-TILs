# from sys import stdin
# n = int(stdin.readline())
# base = [0]+list(map(int, stdin.readline().split()))
# #A는 j, B는 j, C는 total-2*j
# total = sum(base)


# #메모리 초과, 3차원 DP
# # #dp[i][j][k] : i번째까지 봤을 때 A의 합이 j, B의 합이 k
# # dp = [[[False]*(total+1) for _ in range(total+1)] for _ in range(n+1)]
# # dp[0][0][0] = True
# # # print(len(dp), len(dp[0]), len(dp[0][0])) #1~n*0~total*0~total

# # for i in range(1,n+1):
# #     elem = base[i]

# #     #이전인 i-1에서 A그룹에 elem을 더하는 경우
# #     for k in range(total+1):
# #         for j in range(total+1, elem-1, -1):
# #             if dp[i-1][j-elem][k]:
# #                 dp[i][j][k] = True

# #     #이전인 i-1에서 B그룹에 elem을 더하는 경우
# #     for j in range(total+1):
# #         for k in range(total+1, elem-1, -1):
# #             if dp[i-1][j][k-elem]:
# #                 dp[i][j][k] = True

# #     #아무것도 없는 A,B그룹에 elem만 더하는 경우
# #     dp[i][elem][0] = True
# #     dp[i][0][elem] = True

# #     #이전에 가능했으면 지금도 가능! C그룹에 버릴 수 있어서!
# #     for j in range(total):
# #         for k in range(total):
# #             if dp[i-1][j][k]:
# #                 dp[i][j][k] = True

# # for check in range(total, -1, -1):
# #     if dp[n][check][check]:
# #         print(check)
# #         break

# #dp[i][j] : i번째 수까지 고려했을 때 그룹 A합 - 그룹 B합 (항상 그룹 A가 크게 하는 건 힘듦, -의 경우가 생략되 버림
# #OFFSET으로 -도 처리!
# OFFSET = total
# dp = [[float("-inf")]*(total*2+1) for _ in range(n+1)] #A의 최댓값을 구하려 함, 따라서 값이 결정되지 않음을 float("-inf")로 정의
# dp[0][OFFSET] = 0
# # print(len(dp), len(dp[0]), len(dp[0][0])) #n+1*total+1*2

# for i in range(1,n+1):
#     elem = base[i]

#     #모두 i-1을 기반으로 연산하여 중복은 발생하지 않음!

#     #C로 인해 이전에 가능했으면 지금도 가능!
#     for j in range(total*2+1):
#         if dp[i-1][j] != float("-inf"):
#             dp[i][j] = max(dp[i][j], dp[i-1][j])

#     # for j in range(total*2+1): #좌측으로 체크할 때 정방향으로 하지 않아도 됨! 모두 i-1을 기준으로 처리하기 때문!
#         #좌측으로 체크, A에 추가되는 경우!
#         if j >= elem and dp[i-1][j-elem] != float("-inf"):
#             # print("왼", j-OFFSET, elem, dp[i-1][j-elem])
#             dp[i][j] = max(dp[i][j], dp[i-1][j-elem]+elem)

#     # for j in range(total*2+1, -1, -1): #우측으로 체크하더라도 역순으로 하지 않아도 됨! 모두 i-1을 기반으로 하기 때문!
#         #우측으로 체크, B에 추가되는 경우!
#         if j+elem <= total*2 and dp[i-1][j+elem] != float("-inf"):
#             # print("오", j-OFFSET, elem, dp[i-1][j+elem])
#             dp[i][j] = max(dp[i][j], dp[i-1][j+elem])

# print(dp[-1][OFFSET])
# # print(OFFSET)
# # for elem in dp:
# #     print(base)
# #     print(elem[:OFFSET])
# #     print(elem[OFFSET])
# #     print(elem[OFFSET+1:])
# #     print()
# # print(dp[-1], OFFSET, dp[-1][OFFSET])

import sys

INT_MIN = -sys.maxsize
OFFSET = 100000

# 변수 선언 및 입력:
n = int(input())
arr = [0] + list(map(int, input().split()))

# 만들 수 있는 최대 합을 계산합니다.
m = sum(arr)

# dp[i][j] : i번째 수까지 고려헀을 떄
#            그룹 A 합 - 그룹 B 합을 j라 했을 때
#            만들 수 있는 최대 그룹 A의 합
dp = [
    [0] * (m + 1 + OFFSET)
    for _ in range(n + 1)
]


def initialize():
    # 최대를 구하는 문제이므로
    # 초기값을 INT_MIN으로 넣어줍니다.
    for i in range(n + 1):
        for j in range(-m, m + 1):
            dp[i][j + OFFSET] = INT_MIN

    # 초기 조건은
    # 아직 아무런 수도 고른적이 없는 경우이므로 
    # 0번째 수까지 고려하여
    # 그룹 A 합 - 그룹 B 합이 0이고 
    # 그룹 A의 합이 0인 경우에 대한 정보 입니다.
    dp[0][0 + OFFSET] = 0


def update(i, j, prev_i, prev_j, val):
    # 불가능한 경우 패스합니다.
    if prev_j < -m or prev_j > m or dp[prev_i][prev_j + OFFSET] == INT_MIN:
        return
    
    dp[i][j + OFFSET] = max(dp[i][j + OFFSET], dp[prev_i][prev_j + OFFSET] + val)


initialize()

# 점화식에 따라 값을 채워줍니다.
for i in range(1, n + 1):
    for j in range(-m, m + 1):
        # Case 1. 그룹 A에 i번째 원소를 추가하여 그룹A-그룹B가 j가 된 경우
        #         dp[i - 1][j - arr[i]] + arr[i] -> dp[i][j]
        update(i, j, i - 1, j - arr[i], arr[i])

        # Case 2. 그룹 B에 i번째 원소를 추가하여 그룹A-그룹B가 j가 된 경우
        #         dp[i - 1][j + arr[i]] -> dp[i][j]
        update(i, j, i - 1, j + arr[i], 0)

        # Case 3. 그룹 C에 i번째 원소를 추가하여 그룹A-그룹B가 j가 된 경우
        #         dp[i - 1][j] -> dp[i][j]
        update(i, j, i  - 1, j, 0)

# n개의 수를 고려하여
# 그룹A-그룹B가 0이 된 경우 중
# 가능한 그룹A 합의 최대값이 답이 됩니다.
print(dp[n][0 + OFFSET])