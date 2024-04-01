from sys import stdin
n, g = list(map(int, stdin.readline().split()))
group = [set(list(map(int, stdin.readline().split()))[1:]) for _ in range(g)]
# print(group)

ans = {1}
for i in range(g):
    if 1 in group[i]:
        group[i].remove(1)

tmp = {1}
while tmp:
    while tmp:
        key = list(tmp)[0]
        ans.add(key)
        tmp.remove(key)
        for i in range(g):
            if key in group[i]:
                group[i].remove(key)

    for i in range(g):
        if len(group[i]) == 1:
            tmp.add(list(group[i])[0])
    # print(tmp)
# print(group)
print(len(ans))