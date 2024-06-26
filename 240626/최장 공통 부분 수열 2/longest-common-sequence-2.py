from sys import stdin
A = stdin.readline().strip()
B = stdin.readline().strip()

len_A = len(A)
len_B = len(B)
#A에서 어디부터 시작할 것 인지가 중요
#dp[i][j] : A에서 i번째, B에서 j번째까지 살펴봤을때 최대 길이
dp = [[-1]*(len_B+1) for _ in range(len_A+1)]

A = "#"+A
B = "#"+B

for i in range(len_A):
    for j in range(len_B):
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j+1], dp[i+1][j])
        if A[i+1] == B[j+1]: #현재 위치에서 연장이 가능!
            dp[i+1][j+1] = max(dp[i][j]+1,1,dp[i+1][j+1])
# print(dp)

i = len_A
j = len_B
ans = []

while i>0 and j>0:
    # print(i,j)
    if dp[i-1][j] < dp[i][j-1]: #j로 올라감
        if dp[i][j-1] != dp[i][j]:
            ans.append(B[j])
        j-=1
    else: #i로 올라감
        if dp[i-1][j] != dp[i][j]:
            ans.append(A[i])
        i-=1

print("".join(ans[::-1]))