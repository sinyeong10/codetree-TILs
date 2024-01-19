from sortedcontainers import SortedSet
from sys import stdin
n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))

base = SortedSet([0])
min_value = float("inf")
for i in range(n):
    base.add(numbers[i]) #값 추가

    #값이 추가되어 변화하는 길이만 체크
    r_index = base.bisect_right(numbers[i])
    l_index = base.bisect_left(numbers[i])-1
    # print(base, r_index, l_index)

    #최소 거리 갱신
    if r_index == len(base): #우측값이 없는 경우
        min_value = min(min_value, numbers[i]-base[l_index])
    else:
        min_value = min(min_value, min(numbers[i]-base[l_index], base[r_index]-numbers[i]))
    
    print(min_value)