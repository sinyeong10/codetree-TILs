from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[0]=1

for i in range(n):
    max_value = 0
    for j in range(i):    
        if base[i] < base[j]: #현재가 이전보다 작을 시만 가져옴!
            max_value = max(max_value, dp[j])
    dp[i] = max_value + 1 #없으면 없는데로 가져온거에 현재를 포함하여 +1함
print(max(dp))