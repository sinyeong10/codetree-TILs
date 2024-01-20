from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

def in_range(i,j):
    return 0<=i<n and 0<=j<n

def go(i, j, direct):
    #여기서 햇갈림.. 이전 위치의 방향이 아니라 진행방향을 기준으로 할 것!
    #2인 \시 좌-상, 우-하 #2-0, 1-3 : (direct+2)%4
    #1인 /시 상-우, 좌-하 #0-3, 1-2 : 3-direct
    dx, dy = [-1,1,0,0], [0,0,-1,1]  #상하좌우
    count = 0
    while True:
        next_x, next_y = i+dx[direct], j+dy[direct] #이전 방향대로 이동
        count += 1
        # print(i, j, direct, next_x, next_y)

        #나오면 끝
        if not in_range(next_x, next_y):
            break

        #진입 후 모양에 따라 변화
        if base_2d[next_x][next_y] == 2:
            direct = (direct+2)%4
        elif base_2d[next_x][next_y] == 1:
            direct = 3-direct
        i, j = next_x, next_y
    # print(i,j, direct, ":", count)
    return count

# go(-1, 2, 1)

max_value = 0
for i in range(n):
    max_value = max(max_value, go(i, -1, 3)) #왼쪽 시작
    max_value = max(max_value, go(i, n, 2)) #오른쪽 시작
for j in range(n):
    max_value = max(max_value, go(-1, j, 1)) #위쪽 시작
    max_value = max(max_value, go(n, j, 0)) #아래쪽 시작
print(max_value)