from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

result = -1
for i in range(n):
    for j in range(n):
        #초기 위치
        # print(i,j)
        for q in range(1, n-i+1):
            for w in range(1, n-j+1):
                # print(i,j, q,w)
                #가능 범위
                tmp = 0
                for e in range(q):
                    for r in range(w):
                        tmp += base[i+q-1][j+w-1]
                if tmp > 0 and q*w > result:
                    result = q*w

print(result)