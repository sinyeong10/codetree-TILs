from sys import stdin
n = int(stdin.readline())
base = stdin.readline().strip()
target = stdin.readline().strip()

total = 0
trans = {"G":"H", "H":"G"}
for i in range(n-1, -1, -1):
    if total % 2 == 0: #의미 없는 변화
        if base[i] != target[i]:
            total += 1
    else: #변화함
        if base[i] == target[i]:
            total += 1
print(total)