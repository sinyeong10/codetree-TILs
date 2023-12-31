from sys import stdin
k, n = list(map(int, stdin.readline().split()))
answer = []

def solve():
    if len(answer)==n:
        for elem in answer:
            print(elem, end=" ")
        print()
        return
    for i in range(1, k+1):
        answer.append(i)
        solve()
        answer.pop()

solve()