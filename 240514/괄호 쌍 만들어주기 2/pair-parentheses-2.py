#완전 탐색
# from sys import stdin
# base = stdin.readline().strip()
# n = len(base)
# cnt = 0
# for i in range(n-1):
#     for j in range(i+2, n-1):
#         if base[i]==base[i+1]=="(" and base[j]==base[j+1]==")":
#             cnt += 1
# print(cnt)

#한방향 처리!
from sys import stdin
A = stdin.readline().strip()
n = len(A)

cnt = 0
result = 0
for i in range(n-1,0,-1): #마지막인 0은 이미 1에서 같이 확인됨
    if A[i] == ")" and A[i-1] == ")":
        cnt += 1
    elif A[i] =="(" and A[i-1]=="(":
        result += cnt
print(result)