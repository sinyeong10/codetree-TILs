from sys import stdin
n, m = list(map(int, stdin.readline().split()))
point = list(map(int, stdin.readline().split()))
point.sort()

def lower_bound(num):
    left = 0
    right = n-1
    min_idx = n
    while left <= right:
        mid = (left+right)//2
        if point[mid] >= num:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = right + 1
    return min_idx

def upper_bound(num):
    left = 0
    right = n-1
    min_idx = n
    while left <= right:
        mid = (left+right)//2
        if point[mid] > num:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1
    return min_idx

def find(s, e):
    l = lower_bound(s) #이상인 가장 빠른 위치!
    s = upper_bound(e) #초과인 가장 빠른 위치!
    return s-l #없으면 n-n으로 0이 나옴!

for _ in range(m):
    s,e = list(map(int, stdin.readline().split()))
    print(find(s,e))