from sys import stdin
n, m = list(map(int, stdin.readline().split()))

base = []
for _ in range(n):
    w,v = list(map(int, stdin.readline().split()))
    e = v/w #무게 1당 가치를 계산해야함 따라서 가치를 무게로 나눔
    base.append((-e, w, v))

base.sort()

total = 0
value = 0
for e, w, v in base:
    if total+w <= m:
        total += w
        value += v
    else:
        tmp_w = m-total
        total += tmp_w
        value += tmp_w*-e
    if total == m:
        break
    # print(e,w,v)
    # print(total, value)
print(f"{value:.3f}")