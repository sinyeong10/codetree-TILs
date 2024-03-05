from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [False]*n

ans = []
import sys
def check(ans):
    min_value = sys.maxsize
    for i in range(n):
        min_value = min(min_value, base_2d[i][ans[i]])
    return min_value

def solve(cnt): #현재 cnt개를 선택
    max_value = 0
    if cnt == n:
        max_value = max(max_value, check(ans))
        return max_value
    
    for j in range(n): #행은 반드시 하나씩 가져와야하므로 cnt와 동일
        if visited[j]:
            continue
        ans.append(j)
        visited[j] = True
        max_value = max(max_value, solve(cnt+1))
        ans.pop()
        visited[j] = False
    return max_value
print(solve(0))