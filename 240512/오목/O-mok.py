from sys import stdin
n = 19
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def find(i, j):
    global check
    # print(i,j)
    key = base_2d[i][j]
    direct_x, direct_y = [0,1,1,1], [1,0,1,-1] #오른쪽, 아래, 우하단 체크! , 좌 하단 체크
    for x, y in zip(direct_x, direct_y):
        check = True
        for k in range(1, 5):
            if key != base_2d[i+x*k][j+y*k]:
                # print(i+x*k, j+y*k,key, base_2d[i+x*k][j+y*k])
                check = False
                break
        if check:
            # print("정답", i+1+x*2,j+1+y*2)
            print(key)
            print(i+1+x*2,j+1+y*2)
            return

check = False
for i in range(n):
    for j in range(n):
        if base_2d[i][j] != 0 and not check:
            find(i,j)
if not check:
    print(0)

#전역변수인 check를 처리할 다른 방법.....
#sys.exit()를 쓰지 않고 답이 나올때 더 이상 돌지 않을 방법
#다 돌아보고 없을 때 0을 출력할 방법