from sys import stdin
n, k, b = list(map(int, stdin.readline().split()))
base = [0 for _ in range(n+1)]
for _ in range(b):
    num = int(stdin.readline())
    base[num] = 1 #빠진 수

# print(base)

prefix = [0 for _ in range(n+1)] #현재 숫자까지 연속이 되기 위해 필요한 숫자
for i in range(n): #base의 값이 1부터 시작인데 0부터 있어서 i+1로 해야함!
    prefix[i+1] = prefix[i]+base[i+1]

# print(prefix)

min_value = b
for i in range(n-k+1): #인덱스가 숫자를 의미해서 범위가 n까지임!
    # print(f"{i+1}~{i+k}까지 연속되기 위해 필요한 수 : {prefix[i+k]-prefix[i]}")
    min_value = min(min_value, prefix[i+k]-prefix[i]) #i+1부터 i+k까지 k개의 숫자 체크
print(min_value)