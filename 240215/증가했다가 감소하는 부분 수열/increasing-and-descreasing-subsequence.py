from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

dp = [[0]*2 for _ in range(n)]

for i in range(n): #i까지의 최대 기록
    dp[i][0] = 1 #증가!
    dp[i][1] = 1 #감소!

    for j in range(i): #이전의 기록중 계속 감소인지, 증가인지 처리
        if base[j] < base[i]: #계속 증가시
            dp[i][0] = max(dp[i][0], dp[j][0]+1)

        if base[j] > base[i]: #계속 감소시
            dp[i][1] = max(dp[i][1], dp[j][1]+1)
    
    dp[i][1] = max(dp[i][0], dp[i][1]) #감소하는 경우는 앞이 증가하다 감소할 수 있음!

# print(dp)
max_value = 0
for i in range(n):
    for j in range(2):
        max_value = max(max_value, dp[i][j])
print(max_value)

# #dp 변환 상태를 찍어보니... j가 가져올 dp의 값 기준으로 큰지 작은지 처리해서 틀림
# max_value = 0
# for i in range(n): #i 기준으로 꺽임!
#     dp = [0 for _ in range(n)]
#     #처음을 선택하는 경우 한가지!
#     dp[0] = 1

#     #dp를 채워감
#     for q in range(1, n):
#         for j in range(i): #여기는 값이 증가이면 가능
#             if base[q] > base[j]:
#                 dp[q] = max(dp[q], dp[j]+1)
#         for k in range(i, n): #여기는 값이 감소이면 가능
#             if base[q] < base[k]:
#                 dp[q] = max(dp[q], dp[k]+1)
#     # print(i, dp)
#     max_value = max(max_value, max(dp))
# print(max_value)