from sys import stdin
n, t = tuple(map(int, stdin.readline().split()))
time = [int(stdin.readline()) for _ in range(n)]
total = sum(time)
#2명시 172가 127보다 빨리 끝남!, 따라서 순서 유지 필요!

def check(k):
    idx = 0
    total = 0
    tmp = [0]*k
    for i in range(k):
        if idx < n:
            tmp[i] = time[idx]
            idx += 1
    
    while idx < n:
        semi_min = min(tmp)
        for i in range(k):
            tmp[i] -= semi_min
        total += semi_min

        for i in range(k):
            if tmp[i] == 0:
                if idx < n:
                    tmp[i] = time[idx]
                    idx += 1
    total += max(tmp)
    # print(total, sum(time))
    return total <= t #t를 넘지 않게 한다, t이하이다!

left = 1
right = n
min_value = n
while left <= right:
    mid = (left+right)//2
    if check(mid): #가능하면 좌측으로 더 봄
        right = mid-1
        min_value = min(min_value, mid)
    else:
        left = mid+1
print(min_value)