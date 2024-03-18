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
        
#처음 값이 숫자라면 숫자인걸로 조건을 세워 변환할 수도 있음!