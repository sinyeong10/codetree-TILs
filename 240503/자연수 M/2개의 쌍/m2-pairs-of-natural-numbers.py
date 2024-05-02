from sys import stdin
n = int(stdin.readline())
base = {}
for i in range(n):
    x, y = list(map(int, stdin.readline().split()))
    base[y] = x #y값이 x개 존재

key = sorted(base.keys())
# print(base, key)

# ans = 0
# end = n-1 #n개 있고 인덱스 기준!
# for i in range(n): #i는 첫 숫자
#     while base[key[i]] != 0 and i <= end:
#         ans = max(ans, key[i]+key[end])
#         base[key[i]] -= 1
#         base[key[end]] -= 1
#         if base[key[end]] == 0:
#             end -= 1
# print(ans)

#1개 단위를 2개 중 최소단위로 바꿈!
ans = 0
end = n-1 #n개 있고 인덱스 기준!
for i in range(n): #i는 첫 숫자
    while base[key[i]] != 0 and i <= end:
        value = min(base[key[i]], base[key[end]])
        if i == end:
            value // 2
        ans = max(ans, key[i]+key[end])
        base[key[i]] -= value
        base[key[end]] -= value
        if base[key[end]] == 0:
            end -= 1
print(ans)