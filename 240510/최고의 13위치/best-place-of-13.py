from sys import stdin
n = int(stdin.readline())
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n-2): #n-1이 2를 더해서 나올 수 있는 범위까지!
    #n-2까지면 n-3까지 값이 돌아서 처리됨!
        tmp = 0
        for k in range(3):
            if base[i][j+k] == 1:
                tmp += 1
        ans = max(ans, tmp)
print(ans)