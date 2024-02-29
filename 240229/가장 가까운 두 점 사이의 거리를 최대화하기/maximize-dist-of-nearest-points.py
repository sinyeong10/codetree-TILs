from sys import stdin
n = int(stdin.readline())
line = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
line.sort()

def check(dist):
    prev = -dist #dist를 더해도 처음 시작하는 1미만이기 위해서!
    #항상 가장 왼쪽으로 잡아 가능한 쪽으로 가려함!
    for s, l in line:
        if prev + dist > l:
            return False
        #이전 선분의 점인 prev로부터 dist가 더해져서 l이하이므로 현재 선분 중 가장 왼쪽의 값을 지정!
        prev = max(s, prev+dist)
    return True

left = 1
right = 10**9
max_value = 0
while left<=right:
    mid = (left+right)//2
    if check(mid): #가능하면 좀 더 큰 길이가 되는 지 체크하려함!
        max_value = max(max_value, mid)
        left = mid + 1
    else:
        right = mid - 1
print(max_value)