from sys import stdin
n, m = list(map(int, stdin.readline().split()))
A = [stdin.readline() for _ in range(n)]
B = [stdin.readline() for _ in range(n)]

total = 0
def check(idxs):
    global total
    tmpA = set()
    for i in range(n):
        key = ""
        for j in idxs:
            key += A[i][j]
        tmpA.add(key)
    
    for i in range(n):
        key = ""
        for j in idxs:
            key += B[i][j]
        if key in tmpA:
            return 0
    total += 1
    return 1

idxs = []
#굳이 백트래킹 하지 않고, x,y,z를 중복되지 않게 구하는 for문 3중첩도 가능!
def find_idx(idx, cnt):
    if cnt > 4 or idx > m:
        return

    if cnt == 3:
        check(idxs)
        # if check(idxs):
            # print(idxs)
        return


    find_idx(idx+1, cnt)
    idxs.append(idx)
    find_idx(idx+1, cnt+1)
    idxs.pop()

find_idx(0,0)
print(total)