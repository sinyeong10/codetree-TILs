from sys import stdin
n = int(stdin.readline())
base = [int(stdin.readline()) for _ in range(n)]

import sys
ans = sys.maxsize
for i in range(n): #시작하는 방의 위치
    tmp = 0
    dist = 0
    for j in range(i, n): #i부터 시작
        tmp += base[j]*dist
        dist += 1
    for j in range(i): #i전에 끝!
        tmp += base[j]*dist
        dist += 1
    ans = min(ans, tmp)
print(ans)