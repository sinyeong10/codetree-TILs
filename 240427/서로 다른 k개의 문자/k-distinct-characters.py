from sys import stdin
sentense, k = stdin.readline().split()
k = int(k)
check = {}

ans = 0
end = 0
total = 0
for i in range(len(sentense)):
    #범위의 끝까지 다 봤거나 현재 들어갈 위치의 값이 k이상(k)라 더 못들어가는 경우
    # print("f",check)
    while end < len(sentense):# and len(check.keys()) <= k: #k일때 새로운 값은 들어가면 안됨!
        if sentense[end] not in check: #없으면 들어감
            if len(check.keys()) == k:
                break
            check[sentense[end]] = 1
            end += 1
            total += 1
        else:
            check[sentense[end]] += 1
            end += 1
            total += 1
    # print("l", check)
    ans = max(ans, total)
    if check[sentense[i]] == 1:
        del check[sentense[i]]
    else:
        check[sentense[i]] -= 1
    total -= 1
print(ans)