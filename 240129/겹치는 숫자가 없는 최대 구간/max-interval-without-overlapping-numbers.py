from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
count_set = set()

ans = -1
total = 0
j = -1 #현재 위치로 다음 추가는 j+1로 이뤄짐!
for i in range(n):
    while j+1 < n and base[j+1] not in count_set:
        total += 1
        count_set.add(base[j+1])
        j+=1
    ans = max(ans, total)
    count_set.remove(base[i])
    total -= 1
print(ans)