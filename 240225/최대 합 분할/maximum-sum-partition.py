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


#해설보다 2배 빠름
# # 선택한 수를 A, B, C 중 어디 그룹에 넣을지 생각한다
# # j = A-B
# # j+2 = A에 2를 추가한 것 이고, j-2 = B에 2를 추가 한것이다
# # j에 변화가 없으면 C에 추가
# # DP[i][j] = DP[i-1][j-a](A)+a, DP[i-1][j+a](B), DP[i-1][j](C)
# # DP[i][j] 는 A의 합이다

# n = int(input())
# num = [0] + list(map(int, input().split()))
# max_sum = sum(num)
# dp = [[-int(2e9)] * (max_sum * 2) for _ in range(n + 1)]
# dp[0][0] = 0

# for i in range(1, n + 1):
#     a = num[i]
#     for j in range(-max_sum, 0):
#         if j - a >= -max_sum:
#             dp[i][j] = max(dp[i][j], dp[i - 1][j - a] + a)

#         if j + a <= max_sum:
#             dp[i][j] = max(dp[i][j], dp[i - 1][j + a])

#         dp[i][j] = max(dp[i][j], dp[i - 1][j])

#     for j in range(max_sum + 1):
#         if j - a >= -max_sum:
#             dp[i][j] = max(dp[i][j], dp[i - 1][j - a] + a)

#         if j + a <= max_sum:
#             dp[i][j] = max(dp[i][j], dp[i - 1][j + a])

#         dp[i][j] = max(dp[i][j], dp[i - 1][j])

# print(dp[-1][0])

#앞의 코드보다 2배 빠름
# n = int(input())
# arr = [0]+list(map(int, input().split()))
# m = sum(arr)

# # 가능한 합의 경우를 다 구한다
# # 해당 합의 1/2도 존재하는지 알아본다 
# # 존재한다면, 그 max 값이 정답.

# dp = [[0]*(m+1) for _ in range(n+1)]
# dp[0][0] = 1

# for i in range(1, n+1):
#     for j in range(m+1):
#         if j-arr[i]>=0 and dp[i-1][j-arr[i]]>0:
#             dp[i][j] += 1
#         if dp[i-1][j]>0:
#             dp[i][j] += 1
#     # print(arr[i], dp[i])

# result = 0
# for i in range(m, -1, -1):
#     if i%2==0 and dp[n][i]>0 and dp[n][i//2]>1:
#         result = i//2
#         # print(i, i//2)
#         break

# print(result)

from sys import stdin
n = int(stdin.readline())
base = [0]+list(map(int, stdin.readline().split()))
total = sum(base)
OFFSET = total

value = float("-inf")
# import sys
# value = -sys.maxsize
value = -int(2e9)

dp = [[value]*(total*2+1) for _ in range(n+1)]
dp[0][OFFSET] = 0
for i in range(1,n+1):
    elem = base[i]
    for j in range(total*2+1):
        if dp[i-1][j] != value:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j >= elem and dp[i-1][j-elem] != value:
            dp[i][j] = max(dp[i][j], dp[i-1][j-elem]+elem)
        if j+elem <= total*2 and dp[i-1][j+elem] != value:
            dp[i][j] = max(dp[i][j], dp[i-1][j+elem])

print(dp[-1][OFFSET])