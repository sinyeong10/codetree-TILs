from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

#테뷸레이션
def standard(num):
    if base_2d[0][0] < num:
        return 101
    
    #초기 설정!
    maxdp_2d = [[float("inf")]*n for _ in range(n)] #최대값중 최소
    maxdp_2d[0][0] = base_2d[0][0]
    for j in range(1, n):
        if base_2d[0][j] >= num:
            maxdp_2d[0][j] = max(maxdp_2d[0][j-1], base_2d[0][j])
        else: #갈 수 없음!
            break
    for i in range(1, n):
        if base_2d[i][0] >= num:
            maxdp_2d[i][0] = max(maxdp_2d[i-1][0], base_2d[i][0])
        else: #갈 수 없음!
            break
    
    for i in range(1,n):
        for j in range(1,n):
            if base_2d[i][j] >= num:
                maxdp_2d[i][j] = max(min(maxdp_2d[i-1][j], maxdp_2d[i][j-1]), base_2d[i][j]) #위쪽, 왼쪽 중 작은 것과 현재의 최댓값!
    # print(maxdp_2d)
    return maxdp_2d[n-1][n-1] if maxdp_2d[n-1][n-1] != float("inf") else 101



#메모이제이션 시도중....
# def in_range(i,j):
#     return 0<=i<n and 0<=j<n

# def standard(num):
#     if base_2d[0][0] < num:
#         return 101
#     maxdp_2d = [[float("inf")]*n for _ in range(n)] #최대값중 최소
#     def move(i, j, min_value, max_value):
#         # print(i, j, min_value, max_value)

#         # if maxdp_2d[i][j] != float("inf"):
#         #     return maxdp_2d[i][j]
#         if i == n-1 and j == n-1: #도착!
#             maxdp_2d[i][j] = max_value
#             return max_value
            
#         tmp = 101
#         dx, dy = [0,1],[1,0] #오른쪽, 아래 체크
#         for dxs, dys in zip(dx, dy):
#             next_i, next_j = i+dxs, j+dys
#             if in_range(next_i, next_j):
#                 if base_2d[next_i][next_j] >= num: #최솟값 이상이라 이동 가능!
#                     tmp1, tmp2 = min(min_value, base_2d[next_i][next_j]), max(max_value, base_2d[next_i][next_j])
#                     end_max = move(next_i, next_j, tmp1, tmp2)
#                     if end_max != 101:
#                         tmp = min(tmp, end_max)
#                 # else:
#                     # print(i, j, next_i, next_j, base_2d[next_i][next_j])
#         maxdp_2d[i][j] = tmp
#         return tmp
#     a = move(0,0,base_2d[0][0], base_2d[0][0])
#     # print(maxdp_2d)
#     # print(a)
#     return a

#이동할 수 있는 최소 숫자일 때 그 이전의 값에서 더 차이가 최소가 나올 수 있어 더 찾아봐야함!
# min_value = 100
# left = 1
# right = 100
# while left<=right:
#     mid = (left+right)//2
#     tmp = standard(mid)
#     print(mid, tmp)
#     if tmp != 101: #값의 최소가 이 값일 때 이동이 가능함!
#         min_value = min(min_value, tmp-mid)
#         left = mid+1
#     else:
#         right = mid-1
# print(min_value)

# print(standard(1))
# print(standard(2))

min_value = 100
for i in range(1, 100):
    tmp = standard(i)
    print(i, tmp)
    if tmp != 101:
        min_value = min(min_value, tmp-i)
    else:
        break
print(min_value)




#이진탐색 : 시간초과
# def in_range(i,j):
#     return 0<=i<n and 0<=j<n

# def standard(num):
#     def move(i, j, min_value, max_value):
#         # print(i, j, min_value)
#         if i == n-1 and j == n-1:
#             return True
            
#         dx, dy = [0,1],[1,0] #오른쪽, 아래 체크
#         for dxs, dys in zip(dx, dy):
#             next_i, next_j = i+dxs, j+dys
#             if in_range(next_i, next_j):
#                 tmp1, tmp2 = min(min_value, base_2d[next_i][next_j]), max(max_value, base_2d[next_i][next_j])
#                 if abs(tmp2 - tmp1) <= num:
#                     if move(next_i, next_j, tmp1, tmp2):
#                         return True
#         return False
#     return move(0,0,base_2d[0][0], base_2d[0][0])

# min_value = 100
# left = 1
# right = 100
# while left<=right:
#     mid = (left+right)//2
#     if standard(mid): #이정도 차이로 이동이 가능함!
#         min_value = min(min_value, mid)
#         right = mid-1
#     else:
#         left = mid+1
# print(min_value)

# print(standard(19))
# print(standard(20))
# print(standard(21))









#2차원 (최소, 최대) DP 반례가 존재
# 2 4 2 
# 2 1 2 
# 2 1 4
# dp_2d = [[(100, 1)]*n for _ in range(n)] #최소 최대로 갱신!

# #항상 지나가는 점!
# # min_value, max_value = min(base_2d[0][0], base_2d[-1][-1]), max(base_2d[0][0], base_2d[-1][-1])
# min_value, max_value = base_2d[0][0], base_2d[0][0]
# dp_2d[0][0] = (min_value, max_value)
# for j in range(1,n):
#     min_value, max_value = dp_2d[0][j-1]
#     min_value = min(min_value, base_2d[0][j])
#     max_value = max(max_value, base_2d[0][j])
#     dp_2d[0][j] = (min_value, max_value)

# for i in range(1, n):
#     min_value, max_value = dp_2d[i-1][0]
#     min_value = min(min_value, base_2d[i][0])
#     max_value = max(max_value, base_2d[i][0])
#     dp_2d[i][0] = (min_value, max_value)

# dx, dy = [0,-1],[-1,0] #왼쪽, 위 체크

# #항상 차이가 최소인 경우를 선택하면 안됨... (1,2)지만 나중에 (2,4)가 숫자 5와 만나 더 최소가 될 수 있음...
# for i in range(1, n):
#     for j in range(1, n):
#         standard = float("inf")
#         for dxs, dys in zip(dx, dy):
#             prev_i, prev_j = i+dxs, j+dys
#             min_value, max_value = dp_2d[prev_i][prev_j]
#             if standard > max_value-min_value: #차이가 더 작으면 갱신
#                 standard = max_value - min_value #이걸로 기준이 바껴서 이전보다 작을 시 반영
#                 min_value = min(min_value, base_2d[i][j])
#                 max_value = max(max_value, base_2d[i][j])
#                 dp_2d[i][j] = min_value, max_value

#         # print(i,j)
# # for elem in dp_2d:
# #     print(*elem)

# a,b = dp_2d[-1][-1]
# print(b-a)