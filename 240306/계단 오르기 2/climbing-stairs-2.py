from sys import stdin
n = int(stdin.readline())
coin = list(map(int, stdin.readline().split()))
dp = [[-1]*4 for _ in range(n+1)] #i는 현재까지 올라간 계단, j는 1계단 올라간 횟수!

dp[0][0] = 0
dp[1][1] = coin[0]

for i in range(2,n+1):
    if dp[i-2][0] != -1:
        dp[i][0] = dp[i-2][0]+coin[i-1]
    for j in range(1, 4):
        dp[i][j] = max(dp[i-1][j-1], dp[i-2][j])
        if dp[i][j] != -1:
            dp[i][j] += coin[i-1]

# for elem in dp:
#     print(*elem)
print(max(dp[-1]))

#검증
# # from sys import stdin
# # n = int(stdin.readline())
# # base = list(map(int, stdin.readline().split()))
# # print(base, sum(base))

# # ans = []
# # def sol(idx, cnt):
# #     # print(idx, cnt)
# #     if cnt > 3:
# #         return

# #     if ans and ans[-1] == n:
# #         tmp = 0
# #         for i in range(len(ans)):
# #             tmp += base[ans[i]-1] #인덱스 단위로
# #         print(idx, cnt, ans, tmp)
# #         return
    
# #     if idx > n:
# #         return
    
# #     ans.append(idx) #층단위로
# #     sol(idx+1, cnt+1)
# #     sol(idx+2, cnt)
# #     ans.pop()
# #     return
# # print("1시작")
# # sol(1,1)
# # print("2시작")
# # sol(2,0)

#문제의 오류 발견!
# from itertools import combinations

# numbers = [9, 7, 7, 7, 15, 17, 5, 13, 16, 14, 18, 19]
# target_sum = 98

# # 주어진 리스트에서 합이 98이 되는 조합 찾기
# for r in range(1, len(numbers) + 1):
#     for combination_indices in combinations(range(len(numbers)), r):
#         combination = [numbers[i] for i in combination_indices]
#         if sum(combination) == target_sum:
#             if (combination_indices[0] == 0 or combination_indices[0] == 1) and combination_indices[-1] == 12-1:
#                 check = True
#                 last = combination_indices[0]
#                 for elem in combination_indices:
#                     if elem - last > 2:
#                         check = False
#                         continue
#                     else:
#                         last = elem
#                 if check:
#                     print("합이 98이 되는 조합:", combination)
#                     print("인덱스:", combination_indices)