from sys import stdin
n = int(stdin.readline())
bomb = []
for _ in range(n):
    score, time = list(map(int, stdin.readline().split()))
    bomb.append((time, score))
bomb.sort(lambda x : (x[0], -x[1]))
# print(bomb)

time = 0
total = 0
for i in range(n):
    if bomb[i][0] > time: #아직 시간이 안지남!
        total += bomb[i][1]
        time += 1
print(total)