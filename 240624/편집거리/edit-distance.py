from sys import stdin
A = stdin.readline().strip()
B = stdin.readline().strip()

import sys
max_num = sys.maxsize

#dp[i][j]에서 i는 A의 현재 처리하고 있는 인덱스 위치를 의미, j는 B
dp = [[max_num]*(len(B)+1) for _ in range(len(A)+1)]
dp[0][0] = 0

# #삭제, 삽입, 변환, 그대로의 경우로 나눔! [이후로 값을 뿌리는 형태]
#나중에 마지막에서 뿌리는 방법의 초기값 계산의 형태의 연산이 필요해서 if문이 들어가야함..
# for i in range(len(A)+1):
    # for j in range(len(B)+1):
    #     # if dp[i][j] == max_num:
    #     #     continue
#         if i!=len(A) and j!=len(B) and A[i] == B[j]: #여기서 continue를 넣어도 되는가?
#             dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
#             continue #순서만 다른 경우를 제거하는 것 같음!
        
#         if i != len(A): #A를 삭제하는 경우
#             dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
#         if j != len(B): #A를 삽입하는 경우
#             dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
#         if i != len(A) and j != len(B):
#             dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+1)

# # print(dp)
# print(dp[len(A)][len(B)])



#이전 값을 기준으로 처리
#dp[i][j]에서 i는 A의 현재 처리하고 있는 인덱스 위치를 의미, j는 B
dp = [[0]*(len(B)+1) for _ in range(len(A)+1)] #+1은 현재 숫자가 처리하고 있는 위치이기 때문
#dp값 초기화
dp[0][0] = 0
for i in range(len(A)+1):
    dp[i][0] = i
for j in range(len(B)+1):
    dp[0][j] = j

# A = "#"+A
# B = "#"+B

# #(삭제, 삽입, 변환), 그대로의 경우로 나눔! [이전에서 값을 가져오는 형태]
# for i in range(1, len(A)):
#     for j in range(1,len(B)):
#         # print(i,j)
#         if A[i] == B[j]: #여기서 continue를 넣어도 되는가? 가능(2가지 경우로 나눠지기 때문!)
#             dp[i][j] = dp[i-1][j-1]
#         else:
#             dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
# # print(dp)
# print(dp[len(A)-1][len(B)-1])


#(삭제, 삽입, 변환), 그대로의 경우로 나눔! [이전에서 값을 가져오는 형태]
for i in range(1, len(A)+1):
    for j in range(1,len(B)+1):
        # print(i,j)
        if A[i-1] == B[j-1]: #여기서 continue를 넣어도 되는가? 가능(2가지 경우로 나눠지기 때문!)
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
# print(dp)
print(dp[len(A)][len(B)])