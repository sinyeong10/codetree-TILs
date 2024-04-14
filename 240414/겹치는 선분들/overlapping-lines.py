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
    total += point[i][1]
    if total < k:
        ans += abs(last-point[i][0])
        last = point[i][0]
    elif total == k and point[i][1] == 1: #내려갔다가 올라가며 k가 되는 지점이 범위의 시작점!
        last = point[i][0]
    # print(total, last, point[i], ans)

print(ans)