# from sys import stdin
# n, m = list(map(int, stdin.readline().split()))
# base = list(map(int, stdin.readline().split()))

#1대신 True, False로 정의하면 ==을 하지 않아도 됨!
# dp = [-1]*(m+1)
# dp[0] = 1

# #dict로 해당 key가 있는지 체크하면서 찾아갈 수도 있을듯!
# def sol():
#     for elem in base: #주어진 수를 순차적으로 고려
#         for j in range(m, -1, -1): #역방향으로 안하면 계산한 값을 다시 사용
#             #j를 기준으로 좌측을 보며 채워감
#             #j가 elem보다 크다면 j-elem를 보고 가능하면 elem을 j-elem과 더해서 처리가능!
#             if j >= elem and dp[j-elem] == 1:
#                 dp[j] = 1

#             #j를 기준으로 우측을 보며 채워감
#             #j+elem이 목표인 수 m이하라면 j를 보고 가능하면 elem을 j와 더해서 처리가능!
#             # if dp[j] == 1 and j+elem <= m:
#             #     dp[j+elem] = 1
#         # print(elem, dp)
#     return "Yes" if dp[m] == 1 else "No"

# print(sol())
from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [0]+list(map(int, stdin.readline().split())) #dp의 정의상 고르지 않았을 때의 값이 필요!

#dp[i][j] : 지금까지 i번째까지 고려시 고른 수의 합인 j를 만드는 것이 가능!
dp=[[False]*(m+1) for _ in range(n+1)]
dp[0][0] = True #아무것도 없이 0 가능!

for i in range(1, n+1):
    for j in range(m+1):
        #i번째 수를 선택하여 합이 j가 되는 경우!
        #i-1번째 수까지의 합이 j-base[i]이여야 함
        #j는 base[i]이상이여야 함!
        if j>=base[i] and dp[i-1][j-base[i]]:
            dp[i][j] = True
        
        #i번째 수를 선택하지 않고 j가 되는 경우!
        #i-1번째 수까지의 합이 j여야 함
        if dp[i-1][j]:
            dp[i][j] = True

print("Yes" if dp[n][m] else "No")