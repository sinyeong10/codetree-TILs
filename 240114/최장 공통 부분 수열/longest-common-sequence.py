from sys import stdin
a = stdin.readline().strip()
b = stdin.readline().strip()

dp = [[0]*len(b) for _ in range(len(a))] #dp[i][j]는 a의 i번째 문자, b의 j번째 문자까지의 최장 공통 수열

for i in range(len(b)):
    if a[0] == b[i]: #같은 건 1이고
        dp[0][i] = 1
    else: #다르면 이전 값 그대로!
        dp[0][i] = dp[0][i-1]

for j in range(len(a)):
    if a[j] == b[0]:
        dp[j][0] = 1
    else:
        dp[j][0] = dp[j-1][0]

# for elem in dp:
#     print(*elem)

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]: #같으면 추가됨
            dp[i][j] = dp[i-1][j-1] + 1
        else: #다르면 선택 안하고 a,b중 하나를 선택하지 않은 경우의 최선을 가져옴
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


# for elem in dp:
#     print(*elem)

print(dp[len(a)-1][len(b)-1])