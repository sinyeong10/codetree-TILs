from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [stdin.readline().strip() for _ in range(n)]
base_dict = {}
for i in range(n):
    base_dict[base[i]] = i+1

for _ in range(m):
    query = stdin.readline().strip()
    if query.isdigit():
        print(base[int(query)-1])
    else:
        print(base_dict[query])