from sys import stdin
n, s = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

answer = n+1 #불가능한 값
total = 0
j = 0
for i in range(n): #처음위치, 조건 충족시 계속 이동
    while j<n-1 and total < s: #현재 끝이 아니라면 total이 s넘을때까지 계속 더함
        total += base[j]
        j += 1
    if total >= s: #조건 충족시 계산
        answer = min(answer, j-1-i+1) #j는 다음 j를 가리키고 있음!!
        # print(i, j, total, j-1-i+1)
    total -= base[i]
print(-1 if answer == n+1 else answer)