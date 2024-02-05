from sys import stdin
n = int(stdin.readline())
base = [list(map(int, stdin.readline().split())) for _ in range(n)]
base.sort(key = lambda x : (x[1], x[0])) #문제에서 s<e라는 조건이 있기에 x[1]로만 정렬해도 됨
# print(base)

total = 0
last = 0
for i in range(n):
    if base[i][0] < last: #한 회의가 끝나기 전에 시작하는 회의임
        continue
    #문제의 조건에 따라 마지막과 앞만 비교하면 됨
    # if base[i][1] >= last: #항상 만족, 끝나는 직후에 다른 회의가 불가능할 시 등호 사라짐
    total += 1
    last = base[i][1]
print(total)