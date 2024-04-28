from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))
check = {}

ans = 0
total = 0
end = 0
for i in range(n):
    while end < n: #check에서 해당 값이 없을 수 있음
        if base[end] not in check:
            check[base[end]] = 1
            total += 1
            end += 1
        else:
            if check[base[end]] >= k:
                break
            check[base[end]] += 1
            total += 1
            end += 1
    
    ans = max(ans, total)

    check[base[i]] -= 1
    total -= 1
print(ans)