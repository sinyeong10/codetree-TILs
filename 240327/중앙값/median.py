from sys import stdin
t = int(stdin.readline())
import heapq
for _ in range(t):
    m = int(stdin.readline())
    base = list(map(int, stdin.readline().split()))

    a, b = [], []
    for i in range(m):
        num = base[i]
        # print(num, a,b)
        if not a:
            heapq.heappush(a, -num)

        elif len(a) == len(b): #a에 추가!
            b_min = heapq.heappop(b)
            if b_min >= num:
                heapq.heappush(a, -num)
                heapq.heappush(b, b_min)
            else:
                heapq.heappush(a, -b_min)
                heapq.heappush(b, num)

        elif len(a) > len(b): #b에 추가
            a_max = -heapq.heappop(a)
            if a_max < num:
                heapq.heappush(b, num)
                heapq.heappush(a, -a_max)
            else:
                heapq.heappush(a, -num)
                heapq.heappush(b, a_max)

        if i % 2 == 0:
            tmp = -heapq.heappop(a)
            print(tmp, end=" ")
            heapq.heappush(a, -tmp)
    print()