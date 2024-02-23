# from sys import stdin
# n = int(stdin.readline())
# line = list(map(int, stdin.readline().split()))

# #일정 범위를 토막내어 파는 데 길이에 따라 가치가 다름!
# dp = [-1]*(n+1)
# dp[0] = 0
# for length in range(n): #현재 보는 짜른 길이
#     for i in range(n): #현재 만들려는 가치 i+1
#         if i+1-length-1 >= 0: #이전의 값이 존재
#             dp[i+1] = max(dp[i+1], dp[i+1-length-1]+line[length])
#         dp[i+1] = max(dp[i+1], line[i]) #이전에서 온 값과과 한번에 온 값을 비교
# print(dp[-1])

from sys import stdin
n = int(stdin.readline())
line = [0]+list(map(int, stdin.readline().split())) #길이를 인덱스로 바로 접근할 수 있게 함

#일정 범위를 토막내어 파는 데 길이에 따라 가치가 다름!
dp = [-1]*(n+1)
dp[0] = 0
#위처럼 짜를 길이를 기준으로 전체를 보는 것보다 전체에서 짜를 길이를 보는 것이 좀 더 for문을 적게 돔
for i in range(1,n+1): #현재 만들려는 가치!
    for j in range(1,i+1): #보는 짜른 길이, i까지 볼 수 있음!
        dp[i] = max(dp[i], dp[i-j]+line[j]) #오직 한번에 그 길이는 0과 합산되어 계산됨!
print(dp[-1])