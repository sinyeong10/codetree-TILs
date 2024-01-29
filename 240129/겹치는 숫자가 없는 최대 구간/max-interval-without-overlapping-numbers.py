from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))
count_set = set() #3개 이상이 제한일 경우에는 가능한 모든 숫자를 배열로 만들거나 Dict로 처리해야한다.

ans = -1
total = 0
j = -1 #현재 위치로 다음 추가는 j+1로 이뤄짐!
for i in range(n):
    while j+1 < n and base[j+1] not in count_set: #다음이 끝이 아니고 이전에 없어서 포함해도 되는 경우
        total += 1
        count_set.add(base[j+1])
        j+=1
    ans = max(ans, total)
    count_set.remove(base[i])
    total -= 1
print(ans)