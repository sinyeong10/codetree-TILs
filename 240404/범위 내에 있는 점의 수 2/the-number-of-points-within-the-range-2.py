from sys import stdin
n, q = list(map(int, stdin.readline().split()))
point = list(map(int, stdin.readline().split()))
point.sort()

prefix = {}
count = 1
for i in range(n):
    prefix[point[i]] = count
    count += 1

point.append(100001)
prefix[100001] = count-1
prefix[-1] = 0

# print(prefix)

def find_max(num):
    max_value = n
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right)//2
        # print(left, right, mid, point[mid])
        if point[mid] >= num:
            max_value = min(max_value, mid)
            right = mid-1
        else:
            left = mid+1
    return max_value


def find_min(num):
    min_value = -1
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right)//2
        # print(left, right, mid, point[mid])
        if point[mid] <= num:
            min_value = max(min_value, mid)
            left = mid+1
        else:
            right = mid-1
    return min_value

# print(find_min(1), find_min(2), find_min(4), find_min(7), find_min(9))
# print(find_max(0), find_max(2), find_max(4), find_max(7), find_max(9))

for _ in range(q):
    scope = list(map(int, stdin.readline().split()))
    # print(scope, find_max(scope[0]), find_min(scope[1]))
    print(find_min(scope[1])-find_max(scope[0])+1)

    
    # print(prefix[point[find_min(scope[1])]]-prefix[point[find_max(scope[0]-1)]])