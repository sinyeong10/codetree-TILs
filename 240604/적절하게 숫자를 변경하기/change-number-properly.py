from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

#유사도가 가장 높은 수열 : 값이 유사도
#n이라는 길이, 1~4는 해당 숫자를 선택하는 경우, m 비슷한 수열의 제한 조건

#dp[i][j][k] i는 비슷한 수열의 카운팅, j는 현재 인덱스, k는 1~4중 어떤 숫자인지

dp = [[[-1]*(4) for _ in range(n)] for _ in range(m+2)]

for k in range(4):
    if base[0] == k+1:
        dp[0][0][k] = 1
    else:
        dp[0][0][k] = 0

# print(dp)

for i in range(m+1): #비슷한 수열이 0인 것 부터 m인 것 까지 계산
    for j in range(1, n): #현재 보는 인덱스
        for k in range(4):
            for prev_k in range(4):
                if dp[i][j-1][prev_k] == -1:
                    continue
                tmp = 0
                if k+1 == base[j]:
                    tmp = 1
                if k == prev_k: #이전과 숫자가 같은 경우
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][prev_k]+tmp)
                else: #이전과 숫자가 달라 비슷한 수열의 카운팅횟수 1증가
                    dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j-1][prev_k]+tmp)
    # print(i)
    # print(dp)

print(max(dp[m][-1]))