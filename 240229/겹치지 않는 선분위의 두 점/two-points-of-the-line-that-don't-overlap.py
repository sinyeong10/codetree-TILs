# from sys import stdin
# n, m = list(map(int, stdin.readline().split()))
# point = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
# point.sort() #겹치지 않아서 처음 기준 정렬하면 충분!

# def check(dist):
#     count = 0
#     start = -dist #dist를 더해도 처음 값인 0이하가 되기 위해!
#     for i in range(m):
#         s,l = point[i]
#         if start + dist <= s: #이전 선분의 마지막 점의 위치로부터 dist의 거리가 현재 선분의 처음 위치 이하인 경우!
#             start = s
#             count += 1

#         # #만약 앞의 if문이 안걸렸다면 현재 선분의 시작위치에서 시작 못함!
#         # while start+dist <= l: #최대 l까지 dist씩 계속 이동!
#         #     start += dist
#         #     count += 1
#         tmp = (l-start)//dist
#         if tmp > 0:
#             count += tmp
#             start += tmp*dist
#         if count >= n:
#             return True
#     return False

# left = 1
# import sys
# right = sys.maxsize
# max_value = 0 #n개인 여러 가능한 dist중 가장 큰 값!
# while left<=right:
#     mid = (left+right)//2
#     if check(mid): #n개 이상이므로 dist를 더 크게 해서 다시 체크!
#         max_value = max(max_value, mid)
#         left = mid+1
#     else:
#         right = mid-1
# print(max_value)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lines = []
for _ in range(m):
    a, b = map(int, input().split())
    lines.append((a, b))
lines.sort()

def check(dist):
    cnt = 1
    prev = lines[0][0]
    for start, end in lines:
        if prev + dist > end:
            continue
        if prev + dist < start:
            prev = start
            cnt += 1
        dots = max((end - prev) // dist, 0)
        cnt += dots
        prev += dots * dist
    return cnt >= n

answer = 0
left, right = 1, 10 ** 18
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)