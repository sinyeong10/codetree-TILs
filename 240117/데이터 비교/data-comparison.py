from sys import stdin
n = int(stdin.readline())
sequence1 = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
sequence2 = list(map(int, stdin.readline().split()))

base1 = set(sequence1)

for elem in sequence2:
    if elem in base1:
        print(1, end=" ")
    else:
        print(0, end=" ")