N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 

dp = [[-9999 for j in range(M)] for i in range(N)]

#i번째까지 j개 선택한 경우
#현재 값 포함해야할 경우
#j를 +1로 한다면  dp[i-2][j-1]+numbers[i]
#j를 그대로 한다면 dp[i-1][j]+numbers[i]

#현재 값 미포함인 경우 : 이전 값 중 가장 큰 값 : 바로 다음 값 사용 가능
#dp[i-1][j]

#M은 0~M-1
#N도 0~N-1
dp[0][0] = numbers[0]
for i in range(1,N):
    dp[i][0] = max(numbers[i], dp[i-1][0]+numbers[i])

# print("init check")
# for elem in dp:
#     print(*elem)

for j in range(1,M):
    for i in range(2,N):
        dp[i][j] = max(max(dp[i-2][j-1], dp[i-1][j])+numbers[i], dp[i-1][j])

# print("\nresult")
# for elem in dp:
#     print(*elem)

print(dp[-1][-1])