from sys import stdin
n, m = list(map(int, stdin.readline().split()))
quest = []
total = 0
for _ in range(n):
    e, t = list(map(int, stdin.readline().split()))
    total += e
    quest.append((e,t))

def sol():
    if total < m:
        return -1

    import sys
    value = sys.maxsize
    dp = [value]*(total+1)
    dp[0] = 0
    
    for i in range(len(quest)):
        e, t = quest[i]
        for j in range(total,e-1,-1):
            if dp[j-e] != value:
                dp[j] = min(dp[j], dp[j-e]+t)
        dp[e] = min(dp[e], t)
        # print(i, dp)
    
    for k in range(m, total+1):
        if dp[k] != value:
            return dp[k]

print(sol())