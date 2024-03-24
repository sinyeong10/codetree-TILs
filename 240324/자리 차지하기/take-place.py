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

#마지막에 for문 끝날 때 if문때문에 끝난 건지 불가능해서 끝난 건지 체크
if count[base[-1]] > base[-1]:
    print(i)
else:
    print(i+1)