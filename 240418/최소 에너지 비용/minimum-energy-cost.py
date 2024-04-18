from sys import stdin
n = int(stdin.readline())
waste = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))

l_min = [cost[0]]
for i in range(1, n):
    l_min.append(min(cost[i], l_min[-1]))
# print(l_min)

total = 0
for j in range(n-1):
    total += l_min[j]*waste[j]
print(total)