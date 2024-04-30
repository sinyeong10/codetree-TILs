from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

def check(num): #num이 사용자별 이용시간의 최댓값!
    line = [0 for _ in range(m)]
    count = 0
    for i in range(n):
        if line[count] + base[i] <= num: #들어가도 되면
            line[count] += base[i]
        else:
            count += 1
            if count == m:
                return False
            line[count] = base[i]
    return True


min_value = 1440
left = 1
right = 1440
while left<=right:
    mid = (left+right)//2
    if check(mid): #참이면 시간을 더 줄여봄!
        min_value = min(min_value, mid) #가능한 경우만 갱신!
        right = mid-1
    else:
        left = mid+1
print(min_value)