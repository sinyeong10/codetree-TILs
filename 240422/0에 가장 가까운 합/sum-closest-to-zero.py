from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
base.sort()

import sys
min_value = sys.maxsize
for i in range(n):
    j = n-1
    while j>i+1 and abs(base[i]+base[j])>abs(base[i]+base[j-1]):
        j -= 1
    # print(i,j, base[i]+base[j])
    if j>i:
        # if min_value != abs(base[i]+base[j]):
        #     print(i, j, base[i], base[j], (abs(base[i]+base[j])))
        min_value = min(min_value, abs(base[i]+base[j]))
    else:
        break
print(min_value)