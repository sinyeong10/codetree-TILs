from sys import stdin
n = int(stdin.readline())
base = [int(stdin.readline()) for _ in range(n)]
prefix = [0 for _ in range(n+1)]

for i in range(n):
    prefix[i+1] = (prefix[i]+base[i])%7
# print(base)
# print(prefix)

#시간초과
# max_value = 0
# for i in range(1,n):
#     for j in range(i+1, n):
#         if prefix[j]-prefix[i-1] == 0: #(prefix[j]+7-prefix[i-1])%7 == 0:
#             max_value = max(max_value, j-i+1)
#             # print(j, i, j-i+1) #2~1은 2임
# print(max_value)

max_value = 0
record = {}
for i in range(n):
    if prefix[i] not in record: #처음 인덱스 기록!
        record[prefix[i]] = i
    else: #처음과 현재 인덱스의 차가 현재까지 고른 숫자의 합이 7의 배수인 경우!
        max_value = max(max_value, i-record[prefix[i]])

print(max_value)