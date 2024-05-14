from sys import stdin
base = stdin.readline().strip()
n = len(base)
cnt = 0
for i in range(n-1):
    for j in range(i+2, n-1):
        if base[i]==base[i+1]=="(" and base[j]==base[j+1]==")":
            cnt += 1
print(cnt)