from sys import stdin
base = stdin.readline().strip()
tmp = set()
ans = 0
total = 0
end = 0
for i in range(len(base)):
    while end < len(base) and base[end] not in tmp:
        tmp.add(base[end])
        end += 1
        total += 1
    if end <= len(base): #인덱스가 허용된건지 체크
        # print(tmp)
        ans = max(ans, total)
    tmp.remove(base[i])
    total -= 1
print(ans)

# #연속부분문자열
# tmp = set(base)
# print(len(tmp))