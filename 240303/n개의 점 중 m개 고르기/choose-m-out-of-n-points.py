from sys import stdin
n, m = list(map(int, stdin.readline().split()))
point= [tuple(map(int, stdin.readline().split())) for _ in range(n)]

ans = []
#먼저 선택 후 가장 먼 거리 최소화!
def check(ans):
    max_value = 0
    for i in range(m):
        for j in range(i+1, m): #이 인덱스는 ans에 대한 인덱스, ans의 값은 point의 인덱스임!
            x1,y1 = point[ans[i]]
            x2,y2 = point[ans[j]]
            # print(i,j, (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
            max_value = max(max_value, (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    return max_value

import sys
def sol(idx, cnt): #현재 idx를 보며 cnt개를 선택
    min_value = sys.maxsize
    if idx == n: #끝까지 다 본 상태
        if cnt == m:
            min_value = check(ans)
            # print(ans, min_value)
        return min_value
    
    min_value = min(min_value, sol(idx+1, cnt))
    if cnt < m: #현재 선택한 갯수가 m미만일 경우 선택
        ans.append(idx)
        min_value = min(min_value, sol(idx+1, cnt+1))
        ans.pop()
    return min_value

print(sol(0,0))