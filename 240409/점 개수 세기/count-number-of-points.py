from sys import stdin
n, q = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

base.sort()

#굳이 딕셔너리로 count 처리 안해도 이진탐색의 인덱스 차이로 계산 가능함
# trans = {}
# count = 1
# for i in range(n):
#     trans[base[i]] = count
#     count += 1

#base기반으로 이진탐색하므로 앞에서 처리하려 했는데 없어도 될듯!
# maxsize = 10^9+1
# trans[maxsize] = n
# trans[-maxsize] = 0
# print(trans)

def find_min(num):
    left = 0
    right = n-1
    max_value = -1
    while left <= right:
        mid = (left+right)//2
        if base[mid] <= num: #해당 숫자 이하인 가장 큰 숫자!
            max_value = max(max_value, mid)
            left = mid+1
        else:
            right = mid-1
    return max_value

def find_max(num):
    left = 0
    right = n-1
    min_value = n
    while left <= right:
        mid = (left+right)//2
        if base[mid] >= num: #해당 숫자이상인 가장 작은 숫자
            min_value = min(min_value, mid)
            right = mid-1
        else:
            left = mid+1
    return min_value

for _ in range(q):
    a,b = list(map(int, stdin.readline().split()))
    #b이하, a-1초과 찾음!
    # print(a,b,":",find_max(a), find_min(b))
    print(find_min(b)-find_max(a)+1) #최소가 없으면 n이 나오고, 최대가 없으면 -1이나와 맞게됨