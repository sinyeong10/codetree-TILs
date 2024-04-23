from sys import stdin
n, k = list(map(int, stdin.readline().split()))

base = {}
for _ in range(n):
    candy, basket = list(map(int, stdin.readline().split()))
    if basket in base:
        base[basket] += candy
    else:
        base[basket] = candy

print(base)

key = sorted(base.keys())
print(key)

max_value = 0
for elem in key:
    total = 0
    #c-k는 elem의미 c는 elem+k의미 c+k는 elem+2*k를 의미
    for i in range(2*k+1): #0~2*k
        if elem+i in base:
            total += base[elem+i]
    max_value = max(max_value, total)
print(max_value)