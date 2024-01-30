from sys import stdin
n, m = list(map(int, stdin.readline().split()))
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

def solve():
    i = -1 #A의 현재 위치, 이후의 값은 i+1로 추가됨
    for j in range(m): #m까지 조건 충족시 이동
        while i+1 < n and A[i+1]!=B[j]: #i가 n-1이하로 끝이 아니고 현재 매칭되지 않음
            i+=1 #따라서 한방향으로 이동하며 탐색
        
        if i+1 == n: #j와 매칭되는 게 없음, 마지막에 매칭이 된다면 n-2로 m-1과 매칭되어야 함
            return False
        else: #찾아서 i,j 모두 이동
            # print(i+1,j)
            i+=1
    return True

if solve():
    print("Yes")
else:
    print("No")