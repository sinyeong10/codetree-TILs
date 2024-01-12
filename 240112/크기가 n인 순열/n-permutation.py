from sys import stdin
n = int(stdin.readline())
visited = [False for _ in range(n+1)] #번째 기준
answer = []

def solve(idx):
    # print(idx, answer)
    if idx == n:
        for elem in answer:
            print(elem, end=" ")
        print()
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        
        answer.append(i)
        visited[i] = True

        solve(idx+1)

        answer.pop()
        visited[i] = False

solve(0)