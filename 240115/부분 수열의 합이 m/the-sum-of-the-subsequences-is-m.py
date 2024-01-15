from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

stand_num = 10001 #원소값의 최소가 1, m의 최대가 만이므로 10001개는 불가능

dp = [stand_num for _ in range(m+1)] #0~m의 수열의 합일 때 원소의 최소 갯수

#초기 값
dp[0] = 0

for j in range(n): #해당 원소를 한번씩만 체크해야함
    for i in range(m, -1, -1): #역순으로 하면 2+2와 같은 경우는 값이 계산되지 않음!
        if base[j] > i or dp[i-base[j]] == stand_num: #동전 가치가 금액보다 큰 경우 패스, 해당 동전 선택 전의 값이 불가능한 경우 패스
            continue
        dp[i] = min(dp[i], dp[i-base[j]]+1)
print(-1 if dp[m] == stand_num else dp[m])