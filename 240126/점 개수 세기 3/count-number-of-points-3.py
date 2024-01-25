from sys import stdin
n, q = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

from sortedcontainers import SortedSet
number_point = SortedSet(base)
# print(number_point)

find_dict = {}
count = 1
for elem in number_point:
    find_dict[elem] = count
    count+=1
find_dict[float("inf")] = n #b가 주어진 값보다 클 수 있음
# print(find_dict)


for _ in range(q):
    a,b = list(map(int, stdin.readline().split()))
    if b in number_point: #있으면 거기까지의 점의 갯수에 a이상의 값중 가장 작은 갯수에서 -1을 빼어 a이전의 점의 갯수를 뺌
        print(find_dict[b] - (find_dict[number_point[number_point.bisect_left(a)]]-1))
    else: #없어서 그것보다 가장 큰 값을 찾음, a이전의 점의 갯수를 뺌
        print(find_dict[number_point[number_point.bisect_right(b)]]-1 - (find_dict[number_point[number_point.bisect_left(a)]]-1))