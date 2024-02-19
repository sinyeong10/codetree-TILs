from sys import stdin
n = int(stdin.readline())
line = [list(map(int, stdin.readline().split())) for _ in range(n)]
line.sort() #앞이 빠른 순서대로 정렬, 이후 빨리 끝나는 순서대로 정렬

def solve(idx, last): #idx까지 봄, 현재 last가 마지막
    if idx == n: #다 보면 선택x로 0을 반환
        return 0
    x, y = line[idx] #현재 보는 선분
    max_value = 0
    if last < x: #이 경우는 idx를 선택해서 다음으로 가능!
        max_value = max(max_value, solve(idx+1, y))+1 #idx를 선택하였기에 1이 증가됨!
    #idx를 선택하지 않는 경우!
    max_value = max(max_value, solve(idx+1, last))
    # print(idx, last, max_value)
    return max_value

print(solve(0, -1))