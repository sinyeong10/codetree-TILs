from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
A = 0
B = 0

import sys
def solve(idx, cnt): #현재 idx를 봄, 현재 A의 갯수
    global A, B
    tmp = sys.maxsize
    if idx == 2*n:
        if cnt == n:
            tmp = abs(A-B)
        return tmp

    A += base[idx]
    tmp = min(tmp, solve(idx+1, cnt+1))
    A -= base[idx]
    B += base[idx]
    tmp = min(tmp, solve(idx+1, cnt))
    B -= base[idx]
    return tmp

print(solve(0, 0))