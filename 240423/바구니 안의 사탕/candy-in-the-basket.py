from sys import stdin
n, k = list(map(int, stdin.readline().split()))

base = {}
for _ in range(n):
    candy, basket = list(map(int, stdin.readline().split()))
    if basket in base:
        base[basket] += candy
    else:
        base[basket] = candy

# print(base)

key = sorted(base.keys())
# print(key)

# #시간 초과
# max_value = 0
# for elem in key:
#     total = 0
#     #c-k는 elem의미 c는 elem+k의미 c+k는 elem+2*k를 의미
#     for i in range(2*k+1): #0~2*k
#         if elem+i in base:
#             total += base[elem+i]
#     max_value = max(max_value, total)
# print(max_value)

end = 0 #현재 들어갈 사탕
max_value = 0
total = 0
for elem in key: #이제 빠질 사탕
    end = max(end, elem)
    #c-k는 elem의미 c는 elem+k의미 c+k는 elem+2*k를 의미
    while elem+2*k >= end:
        if end in base:
            total += base[end]
        end += 1
    # print(elem, end-1, total)
    max_value = max(max_value, total)
    total -= base[elem]
print(max_value)