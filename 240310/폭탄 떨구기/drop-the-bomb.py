from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = [int(stdin.readline()) for _ in range(n)]
base.sort()

def bomb(r):
    last = -1
    total = 0
    for i in range(n):
        if base[i] <= last:
            continue
        else:
            last = base[i]+2*r
            total += 1
    return total

# print(bomb(5))

left = 0
right = n
min_value = n
while left <= right:
    mid = (left+right)//2
    if bomb(mid) <= k:
        min_value = min(min_value, mid)
        right = mid-1
    else:
        left = mid+1
print(min_value)