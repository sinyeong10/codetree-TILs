from sys import stdin
R, C = list(map(int, stdin.readline().split()))
base_2d =[stdin.readline().split() for _ in range(R)]

def move(x,y, cnt):
    # print(x,y,cnt)
    if x == R-1 and y == C-1 and cnt == 3:
        return 1
    
    if cnt >= 3:
        return 0

    tmp = 0
    for i in range(x+1,R):
        for j in range(y+1, C):
            if base_2d[x][y] != base_2d[i][j]:
                tmp += move(i,j,cnt+1)
    return tmp

print(move(0,0,0))