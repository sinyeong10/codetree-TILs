from sys import stdin
n = int(stdin.readline())
base = [0]+list(map(int, stdin.readline().split()))
#A는 j, B는 j, C는 total-2*j
total = sum(base)

#dp[i][j][k] : i번째까지 봤을 때 A의 합이 j, B의 합이 k
dp = [[[False]*(total+1) for _ in range(total+1)] for _ in range(n+1)]
dp[0][0][0] = True
# print(len(dp), len(dp[0]), len(dp[0][0])) #1~n*0~total*0~total
for i in range(1,n+1):
    elem = base[i]
    for k in range(total+1):
        for j in range(total+1, elem-1, -1):
            if dp[i-1][j-elem][k]:
                dp[i][j][k] = True

    for j in range(total+1):
        for k in range(total+1, elem-1, -1):
            if dp[i-1][j][k-elem]:
                dp[i][j][k] = True

    dp[i][elem][0] = True
    dp[i][0][elem] = True
    for j in range(total):
        for k in range(total):
            if dp[i-1][j][k]:
                dp[i][j][k] = True

for check in range(total, -1, -1):
    if dp[n][check][check]:
        print(check)
        break