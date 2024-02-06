from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

trans = {0 : 1, 1 : 0}
total = 0
for i in range(1, n):
    if base[i-1] != 1: #앞이 1이 아니면 현재칸 주변 반전!
        total += 1
        base[i-1] = trans[base[i-1]] #명시적 표시
        base[i] = trans[base[i]]
        if i+1 < n: #마지막 빼고 다 우측에도 반영
            base[i+1] = trans[base[i+1]]

#마지막이 1이면 가능, 아니면 불가능
if base[-1] == 1:
    print(total)
else:
    print(-1)

# def solve():
#     if n == 1: #맨 처음은 누르지 못해서 바로 체크
#         print(-1 if base[0] != 1 else 0)
#         return

#     trans = {0 : 1, 1 : 0}
#     total = 0
#     for i in range(1, n-1):
#         if base[i-1] != 1: #앞이 1이 아니면 현재칸 주변 반전!
#             total += 1
#             #명시적 표시
#             base[i-1] = trans[base[i-1]]
#             base[i] = trans[base[i]]
#             base[i+1] = trans[base[i+1]]
#         # print(base)

#     #마지막 누를 경우 예외처리 #-2보다는 갯수에 영향을 받지 않는 방법이 더 좋은 것 같다.
#     if base[-2] == 0:
#         total += 1
#         base[-2] = trans[base[-2]]
#         base[-1] = trans[base[-1]]
#     # print(base)

#     #마지막이 1이면 가능, 아니면 불가능
#     if base[-1] == 1:
#         print(total)
#     else:
#         print(-1)

# solve()