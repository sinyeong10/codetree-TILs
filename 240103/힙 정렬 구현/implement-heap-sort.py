from sys import stdin
n = int(stdin.readline())
#1~n까지 사용, 이진트리를 찾아가는 규칙 맞추기 위해!
base = [0]+list(map(int, stdin.readline().split()))

#n이란 정보가 있으면 좋다. len(base)로 가는 것이 아니라 거기서 일정 부분만 보기 때문!
def heapify(base, n, i):
    target = i
    l = 2*i #좌측하단
    r = 2*i+1 #우측하단

    if l <= n and base[l] > base[target]:
        target = l

    if r <= n and base[r] > base[target]:
        target = r

    if target != i: #자식이 더 큼!
        base[i], base[target] = base[target], base[i]
        #더 작은 부모로 바꼈으므로 target 위치에서 재귀적으로 다시 확인!
        heapify(base, n, target)

def heap_sort(base, n):
    # print(list(range(n//2, 0, -1)))
    #max-heap만듦
    for i in range(n//2, 0, -1):
        heapify(base, n, i)
        # print(i, base)

    #가장 큰 걸 맨 우측에 옮기고 그거 빼고 다시 max-heap만듦
    #이때는 루트만 바껴서 그것만 함
    for i in range(n, 1, -1):
        # print(i, base)
        base[i], base[1] = base[1], base[i]
        heapify(base, i-1, 1) #같은 for문이므로 n이 아닌 변화하는 i에 기준을 두어야 함!
        # print(i, base)

heap_sort(base, n)
print(*base[1:])