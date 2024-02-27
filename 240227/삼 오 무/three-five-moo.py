from sys import stdin
n = int(stdin.readline())

def check(num):
    return num//3+num//5-num//15 #3의 배수, 5의 배수는 Moo갯수 증가, 15의 배수는 중복으로 Moo갯수 감소!

import sys
min_value = sys.maxsize
left = 1
right = sys.maxsize #N의 범위가 아님.. N보다 클 수 밖에 없음!

while left <= right:
    mid = (left+right)//2
    count = check(mid) #mid까지 Moo의 갯수
    # print(left, mid, right, count, mid-count, min_value)
    if mid-count < n: #mid-count는 숫자의 갯수
        left = mid+1 #이게 n보다 작으므로 mid는 우측으로 더 크게 봐야함!
    else:#if mid-count >= n:
        right = mid-1
        min_value = min(min_value, mid) #check(mid)에서 mid의 여러 값이 같은 결과로 나올 수 있음
print(min_value)