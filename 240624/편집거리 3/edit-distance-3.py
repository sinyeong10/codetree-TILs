# from sys import stdin
# A = stdin.readline().strip()
# B = stdin.readline().strip()

# A = "#"+A
# B = "#"+B

# a, b = len(A), len(B)

# #dp[i][j] i, j번째 값을 처리하기 위해서 필요한 최소 연산횟수
# dp = [[0]*b for _ in range(a)]

# # dp[0][0] = 0
# for i in range(a):
#     dp[i][0] = i
# for j in range(b):
#     dp[0][j] = j

# for i in range(1, a):
#     for j in range(1, b):
#         if A[i] == B[j]:
#             dp[i][j] = dp[i-1][j-1]
#         else:
#             dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1

# # print(dp)
# print(dp[a-1][b-1])

#A,B를 수정하지 않아도 됨!
from sys import stdin
A = stdin.readline().strip()
B = stdin.readline().strip()

a, b = len(A), len(B)

#dp[i][j] i, j번째 값을 처리하기 위해서 필요한 최소 연산횟수
dp = [[0]*(b+1) for _ in range(a+1)]

dp[0][0] = 0
for i in range(1, a+1):
    dp[i][0] = i
for j in range(1, b+1):
    dp[0][j] = j

for i in range(1, a+1):
    for j in range(1, b+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1

# print(dp)
print(dp[a][b])