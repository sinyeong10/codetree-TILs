from sys import stdin
n, m, c = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))
base.sort()

def check(time): #time까지 기다리다 출발
    last = -1
    total = 0
    cnt = 0
    for i in range(n):
        #대기 시간 초과하거나 현재 탑승이 c명이상인 경우
        if base[i] > last or cnt >= c: #새로 탑승
            cnt = 1
            total += 1
            last = base[i] + time
        else: #기존에 탑승
            cnt += 1
        # print(i, "last",last,"total", total,"cnt", cnt)
    return total

# print(check(4))

left = 0
right = 10**9
min_value = 10**9
while left <= right:
    mid = (left+right)//2
    if check(mid) <= m:
        min_value = min(min_value, mid)
        right = mid-1
    else:
        left = mid+1
print(min_value)