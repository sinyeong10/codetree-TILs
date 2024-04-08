from sys import stdin
n, q = list(map(int, stdin.readline().split()))
stone = [int(stdin.readline()) for _ in range(n)] #인덱스 기준

group1 = [0 for _ in range(n+1)]
group2 = [0 for _ in range(n+1)]
group3 = [0 for _ in range(n+1)]

for i in range(n):
    group1[i+1] = group1[i]+1 if stone[i] == 1 else group1[i]
    group2[i+1] = group2[i]+1 if stone[i] == 2 else group2[i]
    group3[i+1] = group3[i]+1 if stone[i] == 3 else group3[i]


for _ in range(q):
    a, b = list(map(int, stdin.readline().split()))
    print(group1[b]-group1[a-1], group2[b]-group2[a-1], group3[b]-group3[a-1])