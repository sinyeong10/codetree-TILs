from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
dp = [0 for _ in range(n)]
dp[0] = 0
for i in range(1, n):
    check = False
    for j in range(i):
        #이전 체크 #base[j]+j >= i으로 j위치에서 점프해서 i를 넘으면 됨
        if base[j] >= i-j: #현재위치에서 떨어진 것 이상의 값일 경우 갱신 시도!
            check = True
            dp[i] = max(dp[i], dp[j]+1)
    if not check: #이전이 다 불가능하면 멈춤!
        break
    # print(i, dp)
print(max(dp))