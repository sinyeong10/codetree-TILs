from sys import stdin
n, m = list(map(int, stdin.readline().split()))
point = [int(stdin.readline()) for _ in range(n)]
point.sort()
import sys
def check(dist): #dist가 최소거리일 때 m개이상이 가능
    start = -sys.maxsize
    cnt = 0
    for i in range( n):
        if point[i] >= start + dist:
            start = point[i]
            cnt += 1
        # print(i, cnt)
    return cnt >= m

left = 1
right = sys.maxsize
ans = 0
while left<=right:
    mid = (left+right)//2
    if check(mid): #
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1
print(ans)