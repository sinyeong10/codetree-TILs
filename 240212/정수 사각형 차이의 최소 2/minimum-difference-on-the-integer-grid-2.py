from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]

def in_range(i,j):
    return 0<=i<n and 0<=j<n

def stardard(num):
    def move(i, j, min_value, max_value):
        # print(i, j, min_value)
        if i == n-1 and j == n-1:
            return True
            
        dx, dy = [0,1],[1,0] #오른쪽, 아래 체크
        for dxs, dys in zip(dx, dy):
            next_i, next_j = i+dxs, j+dys
            if in_range(next_i, next_j):
                tmp1, tmp2 = min(min_value, base_2d[next_i][next_j]), max(max_value, base_2d[next_i][next_j])
                if abs(tmp2 - tmp1) <= num:
                    if move(next_i, next_j, tmp1, tmp2):
                        return True
        return False
    return move(0,0,base_2d[0][0], base_2d[0][0])

min_value = 100
left = 1
right = 100
while left<=right:
    mid = (left+right)//2
    if stardard(mid): #이정도 차이로 이동이 가능함!
        min_value = min(min_value, mid)
        right = mid-1
    else:
        left = mid+1
print(min_value)

# print(stardard(19))
# print(stardard(20))
# print(stardard(21))

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
# for elem in dp_2d:
#     print(*elem)

# a,b = dp_2d[-1][-1]
# print(b-a)