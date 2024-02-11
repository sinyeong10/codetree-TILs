from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp_2d = [[0]*n for _ in range(n)]

dx, dy = [-1,1,0,0], [0,0,-1,1]

def in_range(i,j):
    return 0<=i<n and 0<=j<n

def sol(i,j, total): #i,j에서 시작하는 경우의 갯수
    # print("def :",i, j, total)
    if dp_2d[i][j] != 0: #이미 기록되어있으면 패스
        # print("이미 계산 :",i,j,dp_2d[i][j])
        return dp_2d[i][j]

    tmp = total #i,j 선택됨!
    for dxs, dys in zip(dx, dy):
        next_i, next_j = i+dxs, j+dys
        if in_range(next_i, next_j): #다음이 범위 밖이 아니면!
            if base_2d[i][j] < base_2d[next_i][next_j]: #더 큰 값인 경우!
                tmp = max(tmp, sol(next_i, next_j, total))
    dp_2d[i][j] = tmp+1
    return tmp+1


# sol(2,0,0)
# sol(1,0,0)
# sol(0,0,0)

max_value = 0
for i in range(n):
    for j in range(n):
        max_value = max(max_value, sol(i, j, 0))
print(max_value)

# for elem in dp_2d:
#     print(*elem)