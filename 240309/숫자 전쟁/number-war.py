from sys import stdin
n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))


#이전 상태를 보고 현재 상태를 계산하지 말자... 햇갈림..
# dp = [[-1]*(n) for _ in range(n)] #B의 i번째 카드까지 다 보고, A의 j번째 카드까지 다 봤을 때 B의 최고 점수

# #비교하여 작을 때에 점수를 얻고 작은 카드를 버림!, 같으면 모두 버림, 모두 버리는 선택이 존재
# dp[0][0] = 0
# #처음 비교해서 B가 점수 획득
# if A[0] > B[0]:
#     dp[0][0] = B[0]

# #B가 A[0]보다 계속 작아서 점수 획득
# for i in range(1, n):
#     if B[i] < A[0]: #계속 B가 작으면 점수 누적!
#         dp[i][0] = dp[i-1][0]+B[i]
#     else: #아니면 멈춤!
#         break

# #A가 B[0]보다 계속 작아서 A의 카드가 버려짐
# for j in range(1, n):
#     if A[j] < B[0]:
#         dp[0][j] = dp[0][j-1]
#     else:
#         break

# for elem in dp:
#     print(*elem)

# for i in range(1, n):
#     for j in range(1, n):
#         dp[i][j] = dp[i-1][j-1] #i-1,j-1에서 카드 버리기를 한 경우!
#         #카드 대결을 하는 경우
#         if B[i] > A[j-1]: #A가 버려진 경우
#             dp[i][j] = max(dp[i][j], dp[i][j-1])
#         elif B[i-1] < A[j] and dp[i-1][j] != -1: #B가 버려진 경우, 이전이 가능한 경우!
#             dp[i][j] = max(dp[i][j], dp[i-1][j])
        
#         #가능한 경우에 i,j에서 카드 비교하여 B가 더 작아서 점수 추가됨
#         if B[i] < A[j] and dp[i][j] != -1:
#             dp[i][j] += B[i]

# print(dp[-1][-1])

# for elem in dp:
#     print(*elem)

#현재에서 계산하여 다음으로 보냄!
dp = [[-1]*(n+1) for _ in range(n+1)] #B의 i번째 카드, A의 j번째 카드를 볼 차례일 때 B의 최고 점수

#비교하여 작을 때에 점수를 얻고 작은 카드를 버림!, 같으면 모두 버림, 모두 버리는 선택이 존재
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1: #불가능한 경우는 계산 x
            continue
        #카드 버리기
        dp[i+1][j+1] = dp[i][j]
        #카드 대결
        if B[i] < A[j]:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+B[i])
        elif B[i] > A[j]:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j])

# for elem in dp:
#     print(*elem)

#i가 가장 큰 것에 최댓값이 있을 것!, i가 많이 버려져야 점수가 높음
print(max(dp[-1]))