from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [int(stdin.readline()) for _ in range(n)]
# print(base)
def divide(number):
    total = 0
    for i in range(n):
        total += base[i]//number
    return total #여기서 조건 비교하고 아래에서 함수만 적어도 된다! 가능여부로 표현!

left = 1
right = 100000 #조건에서 가능한 가장 큰 정수
max_value = 0
while left<=right:
    mid = (left+right)//2
    if divide(mid)>=m: #최댓값을 찾아 우측을 더 봄! #여기에 함수만 적어도 된다! 가능여부로 표현!
        max_value = max(max_value, mid)
        left = mid+1
    else:
        right = mid-1
print(max_value)