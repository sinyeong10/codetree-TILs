from sys import stdin
n = int(stdin.readline())
base = [int(stdin.readline()) for _ in range(n)]
s1, e1 = list(map(int, stdin.readline().split()))
s2, e2 = list(map(int, stdin.readline().split()))

def listpop(base, s, e):
    tmp = []
    for i in range(len(base)):
        if s <= i+1 <= e:
            continue
        tmp.append(base[i])
    return tmp

base = listpop(base, s1, e1)
base = listpop(base, s2, e2)
print(len(base))
for elem in base:
    print(elem)