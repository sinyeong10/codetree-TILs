from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

prefix = [0 for _ in range(n)]
prefix[0] = base[0]
for i in range(1, n):
    prefix[i] = prefix[i-1]+base[i]
# print(prefix)

ans = 0
for i in range(n-k+1): #n-k가 마지막!
    # print(i, i+k-1)
    #처음 값 이전에 빈 값이 없어서 처음값이 빼지는 걸 다시 더해줘서 처리
    ans = max(ans, prefix[i+k-1]-prefix[i]+base[i])
print(ans)