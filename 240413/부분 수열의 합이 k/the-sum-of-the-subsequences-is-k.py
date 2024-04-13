from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

prefix = [0 for _ in range(n+1)]

for i in range(n):
    prefix[i+1] = prefix[i]+base[i]

# print(prefix)

count = 0
for i in range(n+1): #i가 0인 경우는 j가 안돌아 자동 제외됨!
    for j in range(i):
        # print(j,i,prefix[i]-prefix[j])
        if prefix[i]-prefix[j] == k:
            count += 1
print(count)