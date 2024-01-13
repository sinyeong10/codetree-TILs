from sys import stdin
n,m = list(map(int, stdin.readline().split()))
data = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[-1]*n for _ in range(m+1)] #m개의 일, n개의 옷, dp[i][j] 마지막에 j옷을 입으며 i일까지 만족도의 합

#첫날 옷을 입을 수 있는 경우는 초기화
for i in range(n):
    s,e,v = data[i]
    if s<=1<=e:
        dp[1][i] = 0
    
for i in range(2, m+1): #2~m번째 일의 계산
    for j in range(n): #n개의 옷 중 마지막으로 j번째 옷을 입는 경우
        s,e,v = data[j]
        if s<=i<=e: #해당 날짜에 옷을 입을 수 있는 경우 이전을 체크하여 갱신
            max_value = 0
            for k in range(n): #이전 체크
                if dp[i-1][k] == -1: #이전 상태가 불가능한 경우는 패스
                    continue
                max_value = max(max_value, dp[i-1][k] + abs(data[k][2]-v))
            dp[i][j] = max_value

# for elem in dp:
#     print(*elem)

print(max(dp[-1]))