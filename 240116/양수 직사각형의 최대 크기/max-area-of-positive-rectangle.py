from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

def check(i,j): #i,j위치에서 체크
    #현재 위치에서 가로 체크
    count = m-j #마지막 체크안하기 위해서 최대로 설정
    for col in range(m-j):
        if base[i][j+col] <= 0:
            count = col #어차피 1 더해줘야 함
            break
    
    result = -1
    for w in range(n-i): #아래로 내려가며
        for q in range(count): #가로 체크
            if base[i+w][j+q] <= 0:
                break
            result = max(result, (w+1)*(q+1))
        if base[i+w][j] <= 0: #내려갔을때 -면 이후론 불가능
            break
    # print(i,j, "/", result, "/", n-i-1, m-j-1, w, count-1)
    return result

answer=-1
for i in range(n):
    for j in range(m):
        if base[i][j] > 0:
            answer = max(answer, check(i, j))
print(answer)