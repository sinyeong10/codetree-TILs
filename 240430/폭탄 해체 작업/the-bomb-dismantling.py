from sys import stdin
n = int(stdin.readline())
bomb = []
for _ in range(n):
    score, time = list(map(int, stdin.readline().split()))
    bomb.append((score, time))
bomb.sort(lambda x : (-x[1], -x[0]))
# print(bomb)

import heapq
tmp = []

total = 0
time = 10001
for i in range(n): #뒤로 갈수록 빨리 처리해야하는 폭탄이 나옴!
    # print(i, tmp, time, bomb[i], total)
    if time == bomb[i][1]: #같으면 넣음
        # print("같은 시간까지 제한인 폭탄 들어감")
        heapq.heappush(tmp, (-bomb[i][0], bomb[i][1])) #넣을 때는 가중치 우선!
    else: #달라지는 순간에 처리
        if tmp:
            tmp_score, tmp_time = heapq.heappop(tmp)
            # print(-tmp_score, tmp_time, "폭탄이 나옴")
            while tmp and tmp_time < time: #대기가 있고 tmp_time이 현재 시간보다 크면 패스해야함
                # print(-tmp_score, tmp_time,"로 반복문 돔")
                tmp_score, tmp_time = heapq.heappop(tmp)
            if tmp_time >= time:
                total += -tmp_score
        time = bomb[i][1]
        heapq.heappush(tmp, (-bomb[i][0], bomb[i][1]))
# print(i, tmp, time, bomb[i], total)
if tmp:
    tmp_score, tmp_time = heapq.heappop(tmp)
    while tmp and tmp_time < time:
        tmp_score, tmp_time = heapq.heappop(tmp)
    if tmp_time >= time:
        total += -tmp_score
    time = bomb[i][1]
print(total)

    


















# bomb = []
# for _ in range(n):
#     score, time = list(map(int, stdin.readline().split()))
#     bomb.append((time, score))
# bomb.sort(lambda x : (-x[0], -x[1]))
# print(bomb)

# time = bomb[0][0]
# total = 0
# for i in range(n):
#     if time <= bomb[i][0]:
#         total += bomb[i][1]
#         print(bomb[i], time)
#     time -= 1
# print(total)