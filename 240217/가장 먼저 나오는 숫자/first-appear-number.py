from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))
query = list(map(int, stdin.readline().split()))

def find(key):
    left = 0
    right = n-1
    min_idx = n
    while left <= right:
        mid = (left+right)//2
        if base[mid] < key: #우측 영역에 있을 가능성 있음!
            left = mid + 1
        elif base[mid] > key: #좌측 영역에 있을 가능성 있음!
            right = mid - 1
        else:
            min_idx = min(min_idx, mid)
            right = mid-1
    return min_idx+1 if min_idx != n else -1 #번째 단위로 변환 및 없는 경우 처리!

for i in range(m):
    key = query[i]
    print(find(key))