from sys import stdin
A = stdin.readline().strip()
B = stdin.readline().strip()

import sys
max_num = sys.maxsize
#dp[i][j]에서 i는 A의 현재 처리하고 있는 인덱스 위치를 의미, j는 B
dp = [[max_num]*(len(B)+1) for _ in range(len(A)+1)]
dp[0][0] = 0

for i in range(len(A)):
    for j in range(len(B)):
        if dp[i][j] == max_num:
            continue
        if A[i] == B[j]:
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
        
        else:
        #if i != len(A)-1: #A를 삭제하는 경우
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
        #if j != len(B)-1: #A를 삽입하는 경우
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
        #if i != len(A)-1 and j != len(B)-1:
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+1)

print(dp[len(A)-1][len(B)-1])