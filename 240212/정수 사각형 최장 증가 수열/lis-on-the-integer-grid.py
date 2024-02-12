from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp_2d = [[0]*n for _ in range(n)]

dx, dy = [-1,1,0,0], [0,0,-1,1]

def in_range(i,j):
    return 0<=i<n and 0<=j<n

#마지막 루프에서 값이 가장 작아야하므로 total을 전달해서 증가시켜 호출하는 방법은 아님!
def sol(i,j): #i,j에서 시작하는 경우의 갯수
    # print("def :",i, j, total)
    if dp_2d[i][j] != 0: #이미 기록되어있으면 패스
        # print("이미 계산 :",i,j,dp_2d[i][j])
        return dp_2d[i][j]

    #더 갈 수 있는 곳이 있다면 가장 큰 경우를 가져옴
    tmp = 1 #현재 위치
    for dxs, dys in zip(dx, dy):
        next_i, next_j = i+dxs, j+dys
        if in_range(next_i, next_j): #다음이 범위 밖이 아니면!
            if base_2d[i][j] < base_2d[next_i][next_j]: #더 큰 값인 경우!
                tmp = max(tmp, sol(next_i, next_j)+1) #이후의 최대와 현재위치

    dp_2d[i][j] = tmp
    return tmp


# sol(2,0,0)
# sol(1,0,0)
# sol(0,0,0)

max_value = 0
for i in range(n):
    for j in range(n):
        max_value = max(max_value, sol(i, j))
print(max_value)

# for elem in dp_2d:
#     print(*elem)