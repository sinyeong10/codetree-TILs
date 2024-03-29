from sortedcontainers import SortedSet
from sys import stdin
n, m = list(map(int, stdin.readline().split()))
numbers = list(map(int, stdin.readline().split()))

base = SortedSet(list(range(1, m+1)))

for i in range(n):
    if numbers[i] in base:
        base.remove(numbers[i])
    print(base[-1]) #정렬되어있어 max대신 index로 가능!