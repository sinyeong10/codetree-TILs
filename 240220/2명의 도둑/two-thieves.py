from sys import stdin
n, m, c = list(map(int, stdin.readline().split()))
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

def check(idx, total, value): #현재 보는 위치 idx, 지금가지의 무게 total, 보는 공간 value
    max_value = 0
    if idx == len(value):
        return 0
    total += value[idx]
    if total <= c:
        max_value = max(max_value, check(idx+1, total, value))+value[idx]*value[idx]
    total -= value[idx]
    max_value = max(max_value, check(idx+1, total, value))
    return max_value

def choice(x, y): #마지막 선택 위치
    max_value = 0
    ans = (-1,-1)
    for i in range(n):
        for j in range(n): #볼 수 있는 최대시 n-m+1임, m이 1시 다 선택되야 함!
            # print(i,j)
            if (i,j) < (x, y):
                continue
            if i == x and y <= j <= y+m-1: #시작 위치 j가 y~y+m-1에 걸림
                continue
            tmp = []
            for k in range(min(m, n-j)): #j가 0시 n이면 됨!
                # print(base_2d[i][j+k])
                tmp.append(base_2d[i][j+k])
            semi_ans = check(0,0, tmp)
            # print(i,j,tmp, semi_ans)
            if max_value < semi_ans:
                max_value = semi_ans
                ans = (i,j)
    return (*ans, max_value)

a = choice(-1,-1)
b = choice(a[0], a[1])
print(a[-1]+b[-1])