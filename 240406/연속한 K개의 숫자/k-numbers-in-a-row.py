from sys import stdin
n, k, b = list(map(int, stdin.readline().split()))
base = [0 for _ in range(n+1)]
for _ in range(b):
    num = int(stdin.readline())
    base[num] = 1 #빠진 수

# print(base)

prefix = [0 for _ in range(n+1)] #현재 숫자까지 연속이 되기 위해 필요한 숫자
for i in range(n):
    prefix[i+1] = prefix[i]+base[i]

# print(prefix)

min_value = b
for i in range(n-k):
    min_value = min(min_value, prefix[i+k]-prefix[i]) #i+1부터 i+k까지 k개의 숫자 체크
print(min_value)