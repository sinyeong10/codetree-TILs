from sys import stdin
n = int(stdin.readline())
base = [0]+list(map(int, stdin.readline().split()))
total = sum(base)
dp = [[[False]*(total+1) for _ in range(total+1)] for _ in range(n+1)] #i까지 봐서 A의 합이 j, B의 합이 k
# print(len(dp), len(dp[0]), len(dp[0][0]))
dp[0][0][0] = True

for i in range(1, n+1):
    for j in range(total+1):
        for k in range(total+1):
            if dp[i-1][j][k]:
                dp[i][j][k] = True
    
    elem = base[i]
    #이전인 i-1에서 A그룹에 elem을 더하는 경우
    for k in range(total+1):
        for j in range(total+1, elem-1, -1):
            if dp[i-1][j-elem][k]:
                dp[i][j][k] = True

    #이전인 i-1에서 B그룹에 elem을 더하는 경우
    for j in range(total+1):
        for k in range(total+1, elem-1, -1):
            if dp[i-1][j][k-elem]:
                dp[i][j][k] = True

if total%2 == 0 and dp[-1][total//2][total//2]:
    print("Yes")
else:
    print("No")