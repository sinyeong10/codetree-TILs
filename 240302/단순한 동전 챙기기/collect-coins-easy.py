from sys import stdin
n = int(stdin.readline())
base = [stdin.readline().strip() for _ in range(n)]

# def in_range(i,j):
#     return 0<=i<n and 0<=j<n

#그래프 접근이 아니다 본질은 동전의 순서에 있다!
#동전 순서가 결정된다면 동전간의 최단거리가 가능하다!

coin = [[] for _ in range(11)] #처음은 S, 마지막은 E의 위치를 의미
 
for i in range(n):
    for j in range(n):
        if base[i][j] == "S":
            coin[0] = (i,j)
        elif base[i][j] == "E":
            coin[10] = (i,j)
        elif base[i][j] == ".":
            continue
        else:
            coin[int(base[i][j])] = (i,j)
# print(coin)

def diff(A,B):
    return abs(A[0]-B[0])+abs(A[1]-B[1])

import sys
ans = [0]
def solve(idx, cnt, total): #이전에 idx까지 cnt개를 봤고 현재까지의 이동 횟수는 total임!
    # print(idx, cnt, total)
    if idx == 10:
        if cnt < 5: #처음과 마지막을 포함하여 최소 3개이상의 동전이 선택되지 않아서 최댓값 반환!
            total = sys.maxsize
        # print(ans, total)
        return total #가능한 경우는 지금까지 누적되어 계산된 값 반환
        
    tmp = sys.maxsize
    for i in range(idx+1, 11): #이전보다 커지는 방향으로만 가능!
        if coin[i] == []: #없는 숫자는 패스
            continue
        #i를 선택하지 않는 경우
        tmp = min(tmp, solve(i, cnt, total))
        #i를 선택한 경우
        ans.append(i)
        tmp = min(tmp, solve(i, cnt+1, total+diff(coin[ans[-2]], coin[i])))
        ans.pop()
    return tmp

move = solve(0, 1, 0)
print(move if move != sys.maxsize else -1)