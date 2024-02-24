from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
total = sum(base)
#A가 i이면 total-i는 B이고 abs(total-2*i)가 차이임

dp = [False]*(total//2+1) #0~total//2까지 봄, 작은 부분으로 i를 정의! total-i-i가 차이가 됨!
dp[0] = True
for elem in base:
    for j in range(elem, total//2+1): #좌측 기준!, 항상 j는 elem 이상임!
        if dp[j-elem]:
            dp[j] = True
# print(dp)

for tmp in range(total//2, -1, -1): #total~0
    if dp[tmp]:
        print(total-tmp-tmp)
        break