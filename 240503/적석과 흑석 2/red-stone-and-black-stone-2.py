from sys import stdin
c, n = list(map(int, stdin.readline().split()))
T_set = [int(stdin.readline()) for _ in range(c)]
AB_set = [list(map(int, stdin.readline().split())) for _ in range(n)]

T_set.sort()
# 2 2
# 2
# 3
# 1 100
# 2 2
#의 경우 작은 것 부터가 최선이 아님....
#따라서 가장 빨리 끝나는 순서로 정렬함
#[[2, 3], [3, 3], [1, 4]]안됨
#1,3시 불가능
AB_set.sort(key = lambda x : (x[1], x[0]))

# print(T_set, AB_set)
ans = 0
check = 0
for i in range(c):
    while check < n and AB_set[check][0] > T_set[i]:
        check += 1
    # if check < n:
    #     print(T_set[i], AB_set[check])
    if check < n and AB_set[check][0] <= T_set[i] <= AB_set[check][1]:
        ans += 1
        check += 1
    elif check < n and AB_set[check][1] < T_set[i]:
        check += 1
print(ans)