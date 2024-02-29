from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [int(stdin.readline()) for _ in range(m)]

def check(time):
    total = 0
    for elem in base:
        total += time // elem #각 통로를 시간동안 모두 최대한 이용하는 경우
    return total >= n

#1000000000는 통로를 통과하는 최대 시간, 같은 통로를 한번만 이용하는 것이 아니기에 전체 시간은 더 걸릴 수 있음!
import sys
left = 1
right = sys.maxsize
min_value = sys.maxsize
while left<=right:
    mid = (left+right)//2
    if check(mid): #가능 시간을 더 줄여서 최소로 만듦!
        right = mid-1
        min_value = min(min_value, mid)
    else:
        left = mid+1
print(min_value)