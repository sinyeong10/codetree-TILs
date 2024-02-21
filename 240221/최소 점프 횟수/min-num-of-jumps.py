from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

def sol(idx):
    min_value = float("inf")
    if idx == n-1:
        return 0

    # print(idx,base[idx]+1, n-idx)
    for i in range(1, min(base[idx]+1, n-idx)):
        min_value = min(min_value, sol(idx+i)+1)
    return min_value

print(sol(0))