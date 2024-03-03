from sys import stdin
n = int(stdin.readline())
visited = [False]*(n+1) #1~n사용

ans = []

def sol(cnt): #현재 선택한 갯수
    # print(cnt, ans)
    if cnt == n:
        print(*ans)
        return

    for i in range(n, 0, -1): #역순 우선으로 넣어봄
        if visited[i]:
            continue
            
        ans.append(i)
        visited[i] = True

        sol(cnt+1)
        ans.pop()
        visited[i] = False
    return

sol(0)