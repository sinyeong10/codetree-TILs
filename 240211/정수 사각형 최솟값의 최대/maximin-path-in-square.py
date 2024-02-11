from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp_2d = [[0]*n for _ in range(n)]
dp_2d[0][0] = base_2d[0][0]
for j in range(1, n): #우측으로 쭉 최소값나옴
    dp_2d[0][j] = min(dp_2d[0][j-1], base_2d[0][j])

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx, dy = [-1, 0], [0, -1] #위, 좌측 체크

for i in range(1, n):
    for j in range(n):
        min_value = 0 #이전 최솟값중 최대!
        for dxs, dys in zip(dx, dy):
            prev_i, prev_j = i+dxs, j+dys
            if in_range(prev_i, prev_j): #무조건 한번은 되고 범위 안이면 갱신 
                min_value = max(min_value, dp_2d[prev_i][prev_j])
        dp_2d[i][j] = min(base_2d[i][j], min_value) #현재가 최소면 현재를 지나는 경로는 최소!

print(dp_2d[-1][-1])