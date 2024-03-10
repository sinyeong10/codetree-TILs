from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

offset = 20 #-20+offset=0이고 20+offset은 40이 되야함!
dp = [[0]*41 for _ in range(n)] #i번째까지 보고 j-offset의 값임

for i in range(1): #모든 경우를 할 필요 없음, 왜냐하면 모두 활용해야 해서 처음만 설정하면 됨!
    dp[i][base[i]+offset] += 1
    dp[i][-base[i]+offset] += 1

for i in range(1, n):
    for j in range(base[i], 41):
        if dp[i-1][j-base[i]] != 0:
            dp[i][j] += dp[i-1][j-base[i]]
    
    for j in range(41-base[i]):
        if dp[i-1][j+base[i]] != 0:
            dp[i][j] += dp[i-1][j+base[i]]


# for elem in dp:
#     print(*elem)

# for i in range(n):
#     for j in range(41):
#         if dp[i][j] > 0:
#             print(i, j-offset, dp[i][j])

# max_value = 0
# for i in range(n):
#     max_value = max(max_value, dp[i][m+offset])
# print(max_value)
#다돌아야해서 전부 체크 안해도 됨!
print(dp[-1][m+offset])