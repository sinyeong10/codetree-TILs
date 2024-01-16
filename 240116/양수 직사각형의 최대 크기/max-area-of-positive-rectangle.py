from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = [list(map(int, stdin.readline().split())) for _ in range(n)]

#값 한개로 체크하는 i,j위치에서 가로,세로를 통해 box를 계산하는 완전 탐색
# def check(i,j): #i,j위치에서 체크
#     #현재 위치에서 가로 체크
#     count = m-j #마지막 체크안하기 위해서 최대로 설정
#     for col in range(m-j):
#         if base[i][j+col] <= 0:
#             count = col #어차피 1 더해줘야 함
#             break
    
#     result = -1
#     for w in range(n-i): #아래로 내려가며
#         for q in range(count): #가로 체크
#             if base[i+w][j+q] <= 0:
#                 count = q #다음 내려갈 때는 여기까지만 가로 체크 가능
#                 break
#             result = max(result, (w+1)*(q+1)) #인덱스이므로 길이로 바꿔줌
#         if base[i+w][j] <= 0: #내려갔을때 -면 이후론 불가능
#             break
#     # print(i,j, "/", result, "/", n-i-1, m-j-1, w, count-1)
#     return result

# answer=-1
# for i in range(n):
#     for j in range(m):
#         if base[i][j] > 0:
#             answer = max(answer, check(i, j))
# print(answer)

#최대 내려갈 수 있는 길이를 미리 계산해두어 가로로 +1씩 증가하며 그 아래중 min인 값과 곱해서 계산

down_max = [[0]*m for _ in range(n)]

#초기 값, 맨 마지막 행에서부터 올라가며 계산
for j in range(m):
    if base[n-1][j] > 0 :
        down_max[n-1][j] = 1

#down_max 계산
for i in range(n-2, -1, -1):
    for j in range(m):
        if base[i][j] > 0: #아래의 길이에 +1 해줌
            down_max[i][j] = down_max[i+1][j] + 1

#답 계산
result = -1
for i in range(n):
    for j in range(m): #i,j위치에서 탐색
        total_height = float("inf") #최대 길이를 가져와서 바로 처리
        for q in range(j, m):
            total_height = min(total_height, down_max[i][q])
            col_size = q-j+1
            result = max(result, total_height*col_size)
        # print(i, j, total_height, col_size, result)
print(-1 if result == 0 else result) #result가 하나라도 체크하면 0으로 갱신되버림