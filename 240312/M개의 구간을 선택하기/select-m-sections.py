from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

ans = []
import sys
def sol(idx, cnt):
    total = -sys.maxsize

    if cnt == m:
        for i in range(len(ans)):
            total += ans[i]
        # print("값", idx, cnt, ans, total)
        return total

    if cnt > m or idx >= n:
        # print("멈춤", idx, cnt, ans)
        return total
    # print(idx, cnt, ans)
    

    # 현재 인덱스 선택후 계속 선택
    ans.append(base[idx])
    total = max(total, sol(idx+1, cnt))

    #현재 인덱스 선택 후 종료
    total = max(total, sol(idx+2,cnt+1))
    ans.pop()

    #현재 인덱스 선택 안하고 넘어감!
    if ans:
        total = max(total, sol(idx+1, cnt+1))
    return total

print(sol(0,0))