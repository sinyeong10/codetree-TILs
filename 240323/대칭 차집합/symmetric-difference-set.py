from sys import stdin
a, b = list(map(int, stdin.readline().split()))
A = set(map(int, stdin.readline().split()))
B = set(map(int, stdin.readline().split()))
# print(A,B)

ans = 0
for elem in A: #set은 인덱스 순회 불가능!
    if elem not in B: #A-B
        ans += 1

for elem in B:
    if elem not in A: #B-A
        ans += 1

#a+b후 A와 B의 합집합의 갯수 * 2를 빼도 됨!

print(ans)