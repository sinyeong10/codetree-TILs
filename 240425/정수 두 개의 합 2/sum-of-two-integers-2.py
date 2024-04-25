from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = [int(stdin.readline()) for _ in range(n)]
base.sort() #최소, 최대에서 줄어들며 가능한 값 찾기 위함!

ans = 0
end = n-1
for first in range(n):
    while end > first and base[end] + base[first] > k:
        end -= 1 #end가 first와 같아지거나 2수의 합이 k이하가 되면 탈출!
    if base[end] + base[first] <= k: #이하가 되서 while문 탈출인지 조건 위배인지 확인하기 위함!
        ans += end - first #first 선택시 가능한 end의 갯수!
    # print(first, end, base[end],base[first], end-first)


print(ans)