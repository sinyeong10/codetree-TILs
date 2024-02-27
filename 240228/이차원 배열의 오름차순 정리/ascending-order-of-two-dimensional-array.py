from sys import stdin
n = int(stdin.readline())
k = int(stdin.readline())

#당연히 완전탐색은 안됨!
# total = []
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         total.append(i*j)
# total.sort()
# print(total[k-1])

#1~n까지의 범위!
#4의 경우
#1 2 3 4
#2 4 6 8 
#3 6 9 12
#4 8 12 16

#1~mid*mid의 형태로 k미만인 최대, k이상인 최소를 찾고 그 사이의 값에서 k개 이상인 최소를 찾음
# def check(num):
#     ans = 0
#     for i in range(1, n+1):
#         ans += min(num//i, n) #각 행에서 mid값과 비교해 같거나 작은 숫자의 갯수
#     return ans

# #기준 mid를 줘서 midxmid의 갯수로 이진 탐색, k이하인 것 중에서 가장 큰 것을 찾는다!
# left = 0
# right = n
# max_value = 0
# while left<=right:
#     mid = (left+right)//2
#     if check(mid*mid) <= k:
#         max_value = max(max_value, mid*mid)
#         left = mid+1
#     else:
#         right = mid-1
# # print(max_value)

# #k초과인 가장 작은 것을 찾음
# left = 0
# right = n
# import sys
# min_value = sys.maxsize
# while left<=right:
#     mid = (left+right)//2
#     if check(mid*mid) > k:
#         min_value = min(min_value, mid*mid)
#         right = mid-1
#     else:
#         left = mid+1
# # print(min_value)

# # print(max_value, min_value)
# left = max_value
# right = min_value
# ans = sys.maxsize #k이상인 값중 가장 작은값
# while left<=right:
#     mid = (left+right)//2
#     key = check(mid)
#     # print(mid, key)
#     if key < k:
#         left = mid + 1
#     elif key >= k:
#         right = mid - 1
#         ans = min(ans, mid)
# print(ans)

#결국 본질은 이진탐색으로 k이상인 가장 작은 값을 찾는 것!
left = 1
right = n*n
min_value = n*n
while left <= right:
    mid = (left+right)//2
    cnt = 0
    for i in range(n+1):
        cnt += min(mid//i, n) #각 행별로 mid보다 작은 값!

    if cnt >= k: #k이상인 값으로 구간이 잡힘, 이제 좌측에 더 있을 수 도 있어서 최솟값으로 처리, 그래야 배열에서 없는 mid는 제외됨!
        right = mid-1
        min_value = min(min_value, mid)
    else:
        left = mid + 1

print(min_value)