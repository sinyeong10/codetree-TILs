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
for elem in point:
    total += elem[1]
    if total > 1:
        ans += 1
print(ans)