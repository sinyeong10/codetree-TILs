from sys import stdin
n, m = list(map(int, stdin.readline().split()))
jewelry = [list(map(int, stdin.readline().split())) for _ in range(n)]
# jewelry.sort() #작은 순서로 정렬하나 하지 않나 동일 #a+b와 b+a는 동일!

# dp = [-1]*(m+1)
# dp[0] = 0
# for w, v in jewelry: #순차적으로 보석 보는중
#     for j in range(1, m+1): #현재 가치
#         if j >= w and dp[j-w] != -1: #i번째 보석의 무게
#             dp[j] = max(dp[j], dp[j-w]+v)
# print(dp)


dp = [0] * (m + 1) #지금까지 고른 보석 무게의 합이 i일 때 얻을 수 있는 최대 가치
for i in range(1, m + 1):
    # 보석 무게의 합 i를 만들기 위해 마지막으로 길이가 j번 보석을 고른 경우에 얻을 수 있는 최대 가치를 계산
    for w, v in jewelry:
        # i가 현재보는 보석의 무게인 w보다는 같거나 커야만 가능
        if i >= w:
            dp[i] = max(dp[i], dp[i - w] + v)
print(dp[-1])