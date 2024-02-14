from sys import stdin
n = int(stdin.readline())
lines = []
for _ in range(n):
    lines.append(list(map(int, stdin.readline().split())))


#그리디
lines.sort(key = lambda x : x[1]) #마지막 기준으로 정렬
 #(x[1], x[0])로 안해도 됨
 #모두 같은 x2의 값일 경우 선택은 최대 한개라서 x1은 순서대로 하지 않아도 됨!!
# print(lines)

last = -1
total = 0
for x1, x2 in lines:
    if x1 > last:
        last = x2
        total += 1
print(total)

# #dp
# lines.sort() #처음 기준으로 정렬
# # print(lines)

# dp = [0 for _ in range(n)]
# for i in range(n):
#     dp[i] = 1 #해당 선분 선택
#     for j in range(i): #이전의 선분 체크
#         x1_i, _ = lines[i]
#         _, x2_j = lines[j]

#         #처음 기준으로 정렬되어 있음! 끝이 작기만 하면 됨
#         if x2_j < x1_i:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))