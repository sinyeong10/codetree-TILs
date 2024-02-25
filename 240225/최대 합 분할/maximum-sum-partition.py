from sys import stdin
n = int(stdin.readline())
base = [0]+list(map(int, stdin.readline().split()))
#A는 j, B는 j, C는 total-2*j
total = sum(base)


#메모리 초과, 3차원 DP
# #dp[i][j][k] : i번째까지 봤을 때 A의 합이 j, B의 합이 k
# dp = [[[False]*(total+1) for _ in range(total+1)] for _ in range(n+1)]
# dp[0][0][0] = True
# # print(len(dp), len(dp[0]), len(dp[0][0])) #1~n*0~total*0~total

# for i in range(1,n+1):
#     elem = base[i]

#     #이전인 i-1에서 A그룹에 elem을 더하는 경우
#     for k in range(total+1):
#         for j in range(total+1, elem-1, -1):
#             if dp[i-1][j-elem][k]:
#                 dp[i][j][k] = True

#     #이전인 i-1에서 B그룹에 elem을 더하는 경우
#     for j in range(total+1):
#         for k in range(total+1, elem-1, -1):
#             if dp[i-1][j][k-elem]:
#                 dp[i][j][k] = True

#     #아무것도 없는 A,B그룹에 elem만 더하는 경우
#     dp[i][elem][0] = True
#     dp[i][0][elem] = True

#     #이전에 가능했으면 지금도 가능! C그룹에 버릴 수 있어서!
#     for j in range(total):
#         for k in range(total):
#             if dp[i-1][j][k]:
#                 dp[i][j][k] = True

# for check in range(total, -1, -1):
#     if dp[n][check][check]:
#         print(check)
#         break

#dp[i][j] : i번째 수까지 고려했을 때 그룹 A합 - 그룹 B합 (항상 그룹 A가 크게 함!)
dp = [[-1]*(total+1) for _ in range(n+1)]
dp[0][0] = 0
# print(len(dp), len(dp[0]), len(dp[0][0])) #n+1*total+1*2

for i in range(1,n+1):
    elem = base[i]

    #C로 인해 이전에 가능했으면 지금도 가능!
    for j in range(total+1):
        if dp[i-1][j] != -1:
            dp[i][j] = dp[i-1][j]

    for j in range(total+1):
        #좌측으로 체크, A에 추가되는 경우!
        if j >= elem and dp[i-1][j-elem] != -1:
            dp[i][j] = dp[i-1][j-elem]+elem

        #우측으로 체크, B에 추가되는 경우!
        if j+elem <= total and dp[i-1][j+elem] != -1:
            dp[i][j] = dp[i-1][j+elem]

print(dp[-1][0])