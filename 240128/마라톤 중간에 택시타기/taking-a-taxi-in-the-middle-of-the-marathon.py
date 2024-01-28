from sys import stdin
n = int(stdin.readline())
base = [list(map(int, stdin.readline().split())) for _ in range(n)]
L = [0 for _ in range(n)] #왼쪽부터 누적해서 처리됨
R = [0 for _ in range(n)] #오른쪽부터 누적해서 처리됨

for i in range(1, n): #맨 처음은 0임
    x1, y1 = base[i-1]
    x2, y2 = base[i]
    L[i] = L[i-1]+abs(x1-x2)+abs(y1-y2)

for i in range(n-2,-1,-1): #맨 뒤는 0임
    x1, y1 = base[i]
    x2, y2 = base[i+1]
    R[i] = R[i+1]+abs(x1-x2)+abs(y1-y2)

min_value = float("inf")
for i in range(1, n-1): #처음과 마지막은 건너뛰지 않음
    x1, y1 = base[i-1]
    x2, y2 = base[i+1]
    min_value = min(min_value, L[i-1]+R[i+1]+abs(x1-x2)+abs(y1-y2))
print(min_value)