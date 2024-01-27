from sys import stdin
n= int(stdin.readline())

points = []
for _ in range(n):
    a,b  = list(map(int, stdin.readline().split()))
    points.append((a,+1))
    points.append((b, -1))

points.sort()
num = 0
count = 0
for elem, direct in points:
    if direct == +1: #처음시
        if num == 0:
            count+=1
        num+=1
    else: #마지막시
        num-=1

print(count)