from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

count = {}
for i in range(1, m+1):
    count[i] = 0

for i in range(n): #인덱스 단위
    for j in range(base[i], m+1): #번째 단위
        count[j]+=1
    # print(count)
    if count[base[i]] > base[i]:
        break
print(i)