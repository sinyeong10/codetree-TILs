from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]

dp[0] = base[0][:] #복사로 입력함!
# print(dp)

for i in range(1,n): #행을 의미
    for j in range(m): #채울 열을 의미
        for k in range(m): #이전 행의 열을 의미
            if j == k: #이전과 현재의 열이 같으면 패스
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][k]+base[i][j])
# print(dp)
print(max(dp[-1]))