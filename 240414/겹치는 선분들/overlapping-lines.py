from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = 0
point = []
#0~2가 2가 되기 위해 [,)로 인식!
for _ in range(n):
    m1, m2 = stdin.readline().split()
    if m2 == "R":
        point.append((base, +1))
        base += int(m1)
        point.append((base, -1))
    else:
        point.append((base, -1))
        base -= int(m1)
        point.append((base, +1))
point.sort()
# print(point)

ans = 0
total = 0
last = point[0][0]
for i in range(2*n):
    if total >= k:
        ans += point[i][0]-point[i-1][0]
    total += point[i][1]

    # if total == k-1 and point[i][1] == -1: #처음 내려갈 때 계산
    #     ans += abs(last-point[i][0])
    #     last = point[i][0]
    # elif total == k and point[i][1] == 1: #처음 올라갈때 시작 위치 기록
    #     last = point[i][0]
    # # print(total, last, point[i], ans)

print(ans)