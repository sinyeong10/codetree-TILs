from sys import stdin
n = int(stdin.readline())
coin = list(map(int, stdin.readline().split()))
dp = [[-1]*4 for _ in range(n+1)] #i는 현재까지 올라간 계단, j는 1계단 올라간 횟수!

dp[0][0] = 0
dp[1][1] = coin[0]

for i in range(2,n+1):
    #j-1인 경우는 1부터 가능해서! 0인 경우를 따로 처리!
    if dp[i-2][0] != -1:
        dp[i][0] = dp[i-2][0]+coin[i-1]
    for j in range(1, 4):
        dp[i][j] = max(dp[i-1][j-1], dp[i-2][j]) #값이 있으면 -1이 아님
        if dp[i][j] != -1:
            dp[i][j] += coin[i-1]

# for elem in dp:
#     print(*elem)
print(max(dp[-1]))



# #검증
# print(coin, sum(coin))
# #현재 값을 넣어서 까다로움!
# ans = []
# def sol(idx, cnt): #현재 idx층을 이동할 것이며 cnt만큼 1번 이동
#     # print(idx, cnt)
#     if cnt > 3:
#         return

#     if ans and ans[-1] == n:
#         tmp = 0
#         for i in range(len(ans)):
#             tmp += coin[ans[i]-1] #인덱스 단위로
#         print(idx, cnt, ans, tmp)
#         return
    
#     if idx > n:#n층까지 들어가야 해서 그 다음에 출력됨
#         return
    
#     ans.append(idx) #층단위로 #12,2에서 끝인데 여기서 12가 들어가고 다음경우에 끝남!
#     sol(idx+1, cnt+1)
#     sol(idx+2, cnt)
#     ans.pop()
#     return
# # sol(0,0) #현재 층 기준이라 0으로 하려면 다음 층 기준으로 append해야함!
# print("1시작")
# sol(1,1)
# print("2시작")
# sol(2,0)



# #백트래킹
# print("모든 경우")
# ans = []
# def sol(idx, cnt): #현재 idx번째를 보고 한번씩 cnt번 오름
#     if idx > n:
#         return
#     if idx == n:
#         tmp = 0
#         for i in range(len(ans)):
#             tmp += coin[ans[i]-1]
#         print(idx, cnt, ans, tmp)
#         return

#     if idx+2 <= n:
#         ans.append(idx+2)
#         sol(idx+2, cnt)
#         ans.pop()
#     if cnt < 3:
#         ans.append(idx+1)
#         sol(idx+1, cnt+1)
#         ans.pop()
# sol(0,0)



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