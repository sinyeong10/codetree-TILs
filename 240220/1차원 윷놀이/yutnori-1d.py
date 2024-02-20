from sys import stdin
n, m, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

ans=[1 for _ in range(k)] #시작위치가 1임!

def sol(idx): #현재 볼 인덱스를 의미
    total = 0
    if idx == n: #n-1까지 모두 봄
        for elem in ans:
            if elem >= m:
                total += 1
        # print(idx, ans, total)
        return total
    
    for i in range(k):
        ans[i] += base[idx]
        total = max(total, sol(idx+1))
        ans[i] -= base[idx]
    
    return total

print(sol(0))