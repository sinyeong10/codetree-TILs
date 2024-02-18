from sys import stdin
n = int(stdin.readline())
data = [list(map(int, stdin.readline().split())) for _ in range(n)]
data.sort()
# print(data)

dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = data[i][2] #초기 설정 해당 알바만 하는 경우
    #이전에 가능한 경우를 추가함
    for j in range(i): #이전의 끝나는 시간 이후에 시작하는 경우만 가능!
        s, _, p = data[i]
        _, e, _ = data[j]
        if e < s:
            dp[i] = max(dp[j] + p, dp[i])
print(max(dp))