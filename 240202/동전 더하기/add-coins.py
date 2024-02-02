from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = [int(stdin.readline()) for _ in range(n)]

total = 0
for i in range(n-1,-1,-1):
    tmp = k//base[i]
    total += tmp
    k -= tmp*base[i] #k%=base[i]해도 같은 결과를 낼 수 있다!
print(total)