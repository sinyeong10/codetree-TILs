from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

trans = {0 : 1, 1 : 0}
total = 0
for i in range(1, n-1):
    if base[i-1] != 1: #앞이 1이 아니면 현재칸 주변 반전!
        total += 1
        #명시적 표시
        base[i-1] = trans[base[i-1]]
        base[i] = trans[base[i]]
        base[i+1] = trans[base[i+1]]
    # print(base)

#마지막 누를 경우 예외처리
if base[-2] == 0:
    total += 1
    base[-2] = trans[base[-2]]
    base[-1] = trans[base[-1]]
# print(base)

#마지막이 1이면 가능, 아니면 불가능
if base[-1] == 1:
    print(total)
else:
    print(-1)