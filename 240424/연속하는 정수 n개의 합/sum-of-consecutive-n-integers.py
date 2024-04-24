from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

ans = 0
total = 0
end = 0
for first in range(n):
    while total < m and end<n:
        total += base[end]
        end += 1
    if total == m:
        ans += 1
    if total < m: #이후론 빼기만 하므로 불가능해서 탈출!
        break
    total -= base[first] #이상인 경우 앞에서 빼서 다음 경우를 찾음!
    # print(first, end, total) #first를 뺏고 이후 end가 들어감
print(ans)