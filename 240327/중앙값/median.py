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
            #b[0]가 b_min임
            # b_min = heapq.heappop(b)
            if b[0] >= num:
                heapq.heappush(a, -num)
                # heapq.heappush(b, b_min)
            else:
                b_min = heapq.heappop(b)
                heapq.heappush(a, -b_min)
                heapq.heappush(b, num)

        elif len(a) > len(b): #b에 추가
            # a_max = -heapq.heappop(a)
            if -a[0] < num:
                heapq.heappush(b, num)
                # heapq.heappush(a, -a_max)
            else:
                a_max = -heapq.heappop(a)
                heapq.heappush(a, -num)
                heapq.heappush(b, a_max)

        if i % 2 == 0:
            # tmp = -heapq.heappop(a)
            print(-a[0], end=" ")
            # heapq.heappush(a, -tmp)
    print()