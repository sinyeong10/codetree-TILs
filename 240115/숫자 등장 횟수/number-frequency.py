from sys import stdin
n, m = list(map(int, stdin.readline().split()))
numbers = list(map(int, stdin.readline().split()))
base = {}
for i in range(n):
    num = numbers[i]
    if num in base:
        base[num] += 1 #dict에서도 += 연산이 가능
    else:
        base[num] = 1

find_number = list(map(int, stdin.readline().split()))
for j in range(m):
    num = find_number[j]
    if num in base:
        print(base[num], end=" ")
    else:
        print(0, end=" ")