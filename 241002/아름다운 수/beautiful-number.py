from sys import stdin
n = int(stdin.readline())
ans = []
count = 0

def backtrack(cnt):
    if cnt == n:
        check_num()
        return
    
    for i in range(1, 5):
        ans.append(i)
        backtrack(cnt+1)
        ans.pop()

def check_num():
    global count
    # print(count, ans)
    prev = ans[0]
    len_cnt = 0
    for idx in range(n):
        if prev == ans[idx]:
            len_cnt+=1
        else:
            if len_cnt % prev != 0:
                return
            len_cnt = 1
            prev = ans[idx]
    if len_cnt % prev != 0:
        return
    # print(len_cnt)
    count+=1
    # print(count, ans)

backtrack(0)
print(count)