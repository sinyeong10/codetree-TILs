from sys import stdin
s = stdin.readline().strip()
p = stdin.readline().strip()

# new_p = []
# key = "!"
# for j in range(len(p)-1,-1,-1):
#     if p[j] == "*":
#         key = p[j-1]
#         new_p.append(p[j])
#         new_p.append(p[j-1])
#     # if fix and p[j] == key:
#     #     continue
#     elif p[j] != key:
#         new_p.append(p[j])

# # print(new_p)

# p = "".join(new_p[::-1])
# print(p)

# def solve():
#     i_last = len(s)-1
#     j_last = len(p)-1
#     #뒤부터 채워가야  .*a와 같은 경우 처리 가능!
#     while j_last >= 0:
#         # print(i_last, j_last)
#         if i_last < 0:
#             return False
#         if s[i_last] == p[j_last] or p[j_last] == ".":
#             i_last-=1
#             j_last-=1
#         elif p[j_last] == "*":
#             check = True
#             while i_last >= 0 and (p[j_last-1] == s[i_last] or p[j_last-1] == "."):
#                 i_last -= 1
#                 check = False
#             if check:
#                 return False
#             j_last -= 2
#         else:
#             return False
#     return True

# print("true" if solve() else "false")


s = "#"+s
p = "#"+p

s_len = len(s)
p_len = len(p) #특수문자있는 문장

#dp[i][j] : s의 i번째, p의 j번째 숫자까지 가능함!
dp = [[False]*(s_len) for _ in range(p_len)]
dp[0][0] = True

for i in range(p_len-1): #1부터 마지막까지 체크
    for j in range(s_len-1):
        if not dp[i][j]: #이전 i-1, j-1이 가능한 경우
            continue
        
        if i != p_len-2 and p[i+2] == "*": #*인 경우, i+1의 문자를 가지고 처리해야함!
            dp[i+2][j] = True #앞의 문자를 0으로 처리하는 경우!

            for all_check in range(j+1, s_len):
            #왜 범위가 달라지지??
            #여기서 현재 상태까지 문제없는 지 체크한 후에 다음 상태를 +로 처리하기 때문에 값을 바로 가져오는 경우라서 범위에 주의해야 함
            #*앞의 문자를 기준으로 끝까지 비교함
            #다르면 멈춤
                if p[i+1] != "." and s[all_check] != p[i+1]:
                    break
                dp[i+2][all_check] = True
        elif p[i+1] == ".": #.인 경우
            dp[i+1][j+1] = True #다음 숫자 감
        else:
            if s[j+1] == p[i+1]:
                dp[i+1][j+1] = True #다음 숫자 감

# print(dp)

print("true" if dp[p_len-1][s_len-1] else "false")