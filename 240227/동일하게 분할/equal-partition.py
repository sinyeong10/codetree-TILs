from sys import stdin
n = int(stdin.readline())
base = [0]+list(map(int, stdin.readline().split()))
total = sum(base)


#3차원 DP 메모리 초과
# dp = [[[False]*(total+1) for _ in range(total+1)] for _ in range(n+1)] #i까지 봐서 A의 합이 j, B의 합이 k
# # print(len(dp), len(dp[0]), len(dp[0][0]))
# dp[0][0][0] = True

# for i in range(1, n+1):
#     for j in range(total+1):
#         for k in range(total+1):
#             if dp[i-1][j][k]:
#                 dp[i][j][k] = True
    
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

# if total%2 == 0 and dp[-1][total//2][total//2]:
#     print("Yes")
# else:
#     print("No")

#3차원 DP 이전, 현재 상태만 처리 메모리 초과
# dp = [[[False]*(total+1) for _ in range(total+1)] for _ in range(2)] #i까지 봐서 A의 합이 j, B의 합이 k
# # print(len(dp), len(dp[0]), len(dp[0][0]))
# dp[0][0][0] = True

# for idx in range(n):
#     if idx%2 == 0:
#         i = 1
#     else:
#         i = 0

#     for j in range(total+1):
#         for k in range(total+1):
#             if dp[i-1][j][k]:
#                 dp[i][j][k] = True
    
#     elem = base[idx+1]
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
# # print(dp[-1])

# if n%2 == 0:
#     i = 0
# else:
#     i = -1
# if total%2 == 0 and dp[i][total//2][total//2]:
#     print("Yes")
# else:
#     print("No")

# #2차원 DP
# dp = [[-1]*(total+1) for _ in range(n+1)] #dp[i][j] : i번째 수, j는 A그룹의 총합, 값은 B그룹의 총합
# dp[0][0] = 0

# for i in range(1, n+1):
#     elem = base[i]
#     for j in range(total+1): #순방향 #범위를 n으로 해서 틀림...
#         if dp[i-1][j] != -1: #B에 추가
#             dp[i][j] = dp[i-1][j]+elem

#         if j+elem < total and dp[i-1][j] != -1: #A에 추가
#             dp[i][j+elem] = dp[i-1][j]

# # print(total)
# # print(dp)
# if total%2 == 0 and dp[-1][total//2] == total//2:
#     print("Yes")
# else:
#     print("No")

#간단히 total//2를 만들 수 있는 지 확인해도 됨!
#total이 짝수이면 total//2가 되면 다른 그룹은 자동으로 total//2가 됨
value = False
dp = [[value]*(total+1) for _ in range(n+1)] #dp[i][j] : i번째 수, j는 A그룹의 총합
dp[0][0] = True

for i in range(1, n+1):
    elem = base[i]
    for j in range(total+1): #순방향
        if dp[i-1][j] != value: #B에 추가
            dp[i][j] = True

        if j+elem < total and dp[i-1][j] != value: #A에 추가
            dp[i][j+elem] = True

# print(total)
# print(dp)
if total%2 == 0 and dp[-1][total//2]:
    print("Yes")
else:
    print("No")