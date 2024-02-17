from sys import stdin
m = int(stdin.readline())
a,b = list(map(int, stdin.readline().split()))

def find(num):
    left = 1
    right = m
    total = 0
    while left <= right:
        mid = (left + right)//2
        total += 1
        if mid > num: #mid가 num보다 커 num은 mid의 좌측에 있을 가능성이 있음
            right = mid - 1
        elif mid < num:
            left = mid + 1
        else:
            return total

min_value = m
max_value = 0
for num in range(a, b+1):
    tmp = find(num)
    min_value = min(min_value, tmp)
    max_value = max(max_value, tmp)
print(min_value, max_value)