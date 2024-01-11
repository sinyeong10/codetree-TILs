from sys import stdin
k, n = list(map(int, stdin.readline().split()))
result = []

def solve():
    if len(result) == n:
        for elem in result:
            print(elem, end=" ")
        print()
        return

    for num in range(1, k+1):
        if len(result) <= 2 or not(result[-1] == result[-2] == num):
            result.append(num)
            solve()
            result.pop()

solve()