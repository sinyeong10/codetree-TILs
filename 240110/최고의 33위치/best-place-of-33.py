from sys import stdin
n = int(stdin.readline())
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

max_value = 0
for i in range(n-2):
    for j in range(n-2):
        tmp = 0
        for q in range(3):
            for w in range(3):
                tmp += base[i+q][j+w]
        max_value = max(max_value, tmp)
print(max_value)