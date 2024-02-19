from sys import stdin
n, m = list(map(int, stdin.readline().split()))
line = [list(map(int, stdin.readline().split())) for _ in range(m)] #(a,b) a,a+1을 b위치에 이음
line.sort(key=lambda x : (x[1], x[0])) #위에 있고 좌측에 있는 순으로 정렬!

def check(line):
    arrival = [i for i in range(n)] #인덱스는 출발자, 값은 도착지 
    for a, b in line: #가로줄이 겹치는 경우는 없음! #a는 번째 단위
        arrival[a-1], arrival[a] = arrival[a], arrival[a-1] #인덱스 단위로 a를 반영!
    return arrival

answer = check(line)
# print(answer)
path = []

def sol(idx, last, base): #현재 선택한 선분의 수, 마지막 선분의 우측 끝
    min_value = m+1
    if answer[:] == base[:]: #현재 선택한 경우가 가능함!
        min_value = min(min_value, idx)

    if idx == m:
        # if path[:4] == [1,0,2,1]: #예시의 답
        #     print(path)

        # if min_value != m+1: #길이가 m이면서 정답인 경우는 반드시 있음!
        #     print(path)
        return min_value
    for i in range(n-1):
        if last == i+1: #이전과 현재가 같은 경우는 변동이 없어 넘어감!
            continue
        base[i], base[i+1] = base[i+1], base[i]
        path.append(i)
        # print(path, base)
        min_value = min(min_value, sol(idx+1, i+1, base)) #이후 가능한 경우중 최소 가져옴
        path.pop()
        base[i], base[i+1] = base[i+1], base[i]
    return min_value
        
base = [i for i in range(n)]
print(sol(0,-1, base))