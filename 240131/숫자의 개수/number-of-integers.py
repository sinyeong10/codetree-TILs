from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

def bisect_left(num):
    left = 0
    right = n-1
    min_index = n
    while left <= right:
        mid = (left+right)//2
        if num <= base[mid]:
            min_index = min(min_index, mid)
            right = mid-1
        else:
            left = mid+1
    return min_index

def bisect_right(num):
    left = 0
    right = n-1
    min_index = n
    while left <= right:
        mid = (left+right)//2
        if num < base[mid]:
            min_index = min(min_index, mid)
            right = mid-1
        else:
            left = mid+1
    return min_index


for _ in range(m):
    number = int(stdin.readline())
    print(bisect_right(number)-bisect_left(number))