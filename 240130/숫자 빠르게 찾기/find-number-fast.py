from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

def binary_search(number):
    left = 0
    right = n-1
    while left <= right: #=이어야지 left,right같을 때 한번 더 돔
        mid = (right+left)//2
        # print(left, mid, right)

        if base[mid] == number:
            return mid+1 #인덱스를 번째로 변환해서 반환
        
        if number < base[mid]: #number가 base[mid]보다 작아 좌측에 있음!
            right = mid-1
        else: #mid인 경우는 위에서 체크됨, 따라서 우측에 있음!
            left = mid+1

    return -1 #어디도 없음

for _ in range(m):
    number = int(stdin.readline())
    print(binary_search(number))