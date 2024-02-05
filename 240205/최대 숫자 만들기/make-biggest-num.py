from sys import stdin
n = int(stdin.readline())
base = [int(stdin.readline()) for _ in range(n)]

from functools import cmp_to_key

def compare(x, y):
    a, b = str(x), str(y)

    if int(a+b) < int(b+a): #b가 앞으로!
        return 1
    elif int(a+b) > int(b+a): #a가 앞으로!
        return -1
    else:
        return 0 #우선순위 동일

    # #[37,4,43, 45]순으로 나옴 하지만 [45, 4, 43, 37]이여야 함
    # if a > b: #x가 사전순으로 더 뒤
    #     return 1
    # elif a < b:
    #     return -1
    # else: #우선 순위가 동일
    #     return 0

base.sort(key=cmp_to_key(compare))
answer = ""
for elem in base:
    answer += str(elem)
print(answer)