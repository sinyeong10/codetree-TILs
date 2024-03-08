from sys import stdin
n = int(stdin.readline())

from collections import deque
def sol():
    save_point = {}
    q = deque()
    q.append(n)
    save_point[n] = 0

    while q:
        num = q.popleft()
        
        if num == 1:
            break

        tmp = num-1
        if tmp not in save_point:
            save_point[tmp] = save_point[num]+1
            q.append(tmp)
        
        tmp = num+1
        if tmp not in save_point:
            save_point[tmp] = save_point[num]+1
            q.append(tmp)

        if num%2==0:
            tmp = num//2
            if tmp not in save_point:
                save_point[tmp] = save_point[num]+1
                q.append(tmp)
            
        if num%3==0:
            tmp = num//3
            if tmp not in save_point:
                save_point[tmp] = save_point[num]+1
                q.append(tmp)
        # print(save_point)
    return save_point[1]
print(sol())