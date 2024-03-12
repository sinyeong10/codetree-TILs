from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

ans = []
import sys
def sol(idx, cnt):
    total = -sys.maxsize

    if cnt == m: #m-1가 되고 바로 끝나면 안됨!
        total = 0
        for i in range(len(ans)):
            total += ans[i]
        # print("값", idx, cnt, ans, total)
        return total

    if cnt > m or idx >= n: #범위 초과
        # print("멈춤", idx, cnt, ans)
        return total
    # print(idx, cnt, ans)
    
    #현재 값 선택 안하고 넘어감!
    total = max(total, sol(idx+1, cnt))

    # 현재 인덱스 선택
    if ans and ans[-1] != base[idx-1]: #이전 값이 있고, 현재 선택 바로 전의 값이 아닌 경우
        cnt += 1
    if not ans:
        cnt += 1
    ans.append(base[idx])
    total = max(total, sol(idx+1, cnt))
    ans.pop()

    return total

print(sol(0,0))