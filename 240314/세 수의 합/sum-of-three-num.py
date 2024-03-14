from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

count = {}
total = 0
for elem in base:
    diff = k-elem
    if diff in count:
        total += count[diff]
    
    tmp = []
    for still in count.keys():
        # print(still)
        # if still != elem: #값이 같아도 이전에 나온 갯수만 큼 들어감!
        # count[still+elem] = count[still] #순회하면서 수정 불가능!
        tmp.append((still+elem, count[still]))
    
    for idx, value in tmp:
        count[idx] = value
    
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1
print(total)