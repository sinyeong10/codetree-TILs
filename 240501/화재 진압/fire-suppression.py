from sys import stdin
n, m = list(map(int, stdin.readline().split()))
will_fire = list(map(int, stdin.readline().split()))
fire_station = list(map(int, stdin.readline().split()))

will_fire.sort()
fire_station.sort()
# print(will_fire)
# print(fire_station)

max_value = 0
end = 0 #소방서 의미
for i in range(n): #불난 곳 의미
    while end < m-1 and abs(will_fire[i]-fire_station[end]) >= abs(will_fire[i]-fire_station[end+1]):
        end += 1
    max_value = max(max_value, abs(will_fire[i]-fire_station[end]))
    # print(will_fire[i], fire_station[end], abs(will_fire[i]-fire_station[end]))
print(max_value)

# #시간 초과
# import sys
# max_value = 0
# end = 0
# for i in range(n): #화재위치별 소방서 최소 출동시간
#     total = sys.maxsize
#     for j in range(m):
#         total = min(total, abs(will_fire[i]-fire_station[j]))
#     # print(i, total)
#     max_value = max(max_value, total)
# print(max_value)