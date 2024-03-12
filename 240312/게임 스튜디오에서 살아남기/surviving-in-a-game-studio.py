# 1인경우
# (1,0,0):G:1
# (1,0,1):B:1
# (1,1,0):T:1

# 2인경우
# (2,0,0):GG,BG:2 - (1,0,0), (1,0,1)
# (2,0,1):GB:1 - (1,0,0)
# (2,0,2):BB:1 - (1,0,1)
# (2,1,0):GT,TG,BT:3 - (1,0,0),(1,1,0),(1,0,1)
# (2,2,0):TT:1 - (1,1,0)
# (2,1,1):TB:1 - (1,1,0)

# 3인경우
# (3,0,0):GGG,BGG,GBG,BBG:4 - (2,0,0),(2,0,1),(2,0,2)
# (3,0,1):GGB,BGB:2 - (2,0,0)
# (3,0,2):GBB:1 - (2,0,1)
# (3,0,3):BBB:1 - (2,0,2)
# (3,1,0):BBT,GBT,GGT,BGT,BTG,TBG,TGG,GTG:8 - (2,0,2),(2,0,1),(2,0,0),(2,1,0),(2,1,1)
# (3,1,1):GTB,TGB,BTB:3 - (2,1,0)
# (3,1,2):TBB:1 - (2,1,1)
# (3,2,0):GTT,TGT,BTT,TTG,TBT:5 - (2,1,0),(2,2,0),(2,1,1)
# (3,2,1):TTB:1 - (2,2,0)
# (3,3,0):TTT:1 - (2,2,0)

from sys import stdin
n = int(stdin.readline())

dp = [[[0]*3 for _ in range(3)] for _ in range(n)]

dp[0][1][0] = 1 #"T"인 경우
dp[0][0][1] = 1 #"B"인 경우
dp[0][0][0] = 1 #"G"인 경우

#이전 상태에서 값을 가져오며 처리함!
for i in range(1, n):
    for j in range(3):
        for k in range(3):
            # print(i,j,k,end=" : ")
            if i+1 == j: #T가 붙는 경우
                # print("A", end=" : ")
                dp[i][j][k] += dp[i-1][j-1][k]

            elif k == 0: #앞의 if문에서 여기의 예외는 계산되어 빠짐
                # print("B", end=" : ")
                #G가 붙는 경우
                for w in range(3):
                    dp[i][j][k] += dp[i-1][j][w]

                if j == 0: #T가 없는 경우엔 T를 붙일 수 없음!
                    continue
                #T가 붙는 경우
                for w in range(3):
                    dp[i][j][k] += dp[i-1][j-1][w]
            
            elif k != 0: #B가 붙는 경우
                # print("C", end=" : ")
                dp[i][j][k] += dp[i-1][j][k-1]
            # print(dp[i][j][k])
            dp[i][j][k] = dp[i][j][k]%(10**9+7) #각각을 나머지 연산

total = 0
for i in range(3):
    total += sum(dp[-1][i])#%(10**9+7) #sum하다 터질 수 있음
print(total%(10**9+7)) #마지막에 각각을 다 더한 것을 나머지 연산

# print(dp)

# #백트래킹 시간초과
# total = 0
# ans = []
# def sol(idx, cnt):
#     global total
#     if idx == n:
#         total += 1
#         print(ans, cnt)
#         return
    
#     ans.append("G")
#     sol(idx+1, cnt)
#     ans.pop()

#     if cnt < 2: #2번까지 가능!
#         ans.append("T")
#         sol(idx+1, cnt+1)
#         ans.pop()

#     if len(ans) >= 2 and ans[-1] == "B" and ans[-2] == "B":
#         return
#     ans.append("B")
#     sol(idx+1, cnt)
#     ans.pop()

# sol(0, 0)
# print(total%(10**9+7))

# #위를 역으로 바꾼 후 메모이제이션
# memo = {(0,0):0, (0,1):0, (0,2):0, (1,0):2, (1,1):1}
# #(2, 0): 4, (2, 1): 4, (2, 2): 1
# #(3, 0): 7, (3, 1): 12, (3, 2): 6


# ans = []
# def sol(length, cnt, tmp):
#     total = 0
#     if (length, cnt, tmp) in memo:
#         return memo[(length, cnt, tmp)]
    
#     if length == 0 or cnt == -1 or tmp == -1:
#         return 0

#     ans.append("G")
#     for i in range(n):
#         total += sol(length-1, i)
#     ans.pop()

#     ans.append("T")
#     for i in range(n):
#         total += sol(length-1, cnt-1, i)
#     ans.pop()

#     ans.append("B")
#     total += sol(length-1, cnt, tmp-1)
#     ans.pop()

#     memo[(length, cnt, tmp)] = total
#     return total

# print(sol(n, 0, 0))#+sol(n, 1)+sol(n, 2))

# print(memo)