from sys import stdin
n = int(stdin.readline())

check = True
ans = []
def sol(idx):
    global check
    if not check:
        return
    if idx == n:
        for elem in ans:
            print(elem, end="")
        print()
        check = False
        return
    
    for i in range(4,7):
        tmp = True
        if len(ans) >= 1 and i == ans[-1]:
            tmp = False
            continue
        
        for j in range((idx+1)//2-1): #홀수 시 보는 범위 증가!
            # print(ans, i,j,ans[-(3+j)-j:-1-j], ans[-1-j:] + [i])
            if ans[-(3+j)-j:-1-j] == ans[-1-j:] + [i]:
                tmp = False
                break

            # if len(ans) >= 5 and ans[-5:-2] == ans[-2:]- + i:
            #     tmp = False
            #     break
            #...
        if tmp:
            ans.append(i)
            sol(idx+1)
            ans.pop()
    return

sol(0)