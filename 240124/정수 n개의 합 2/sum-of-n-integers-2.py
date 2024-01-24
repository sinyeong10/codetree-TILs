from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

prefix_sum = [0]*(n+1)
prefix_sum[0] = 0
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1]+base[i-1]

# print(prefix_sum)

max_value = 0
for i in range(1, n-k+1): #n-k의 값에 +k-1의 연산이 들어간 인덱스가 n-1이면 된다.
    max_value = max(max_value, prefix_sum[i+k-1]-prefix_sum[i-1])
print(max_value)