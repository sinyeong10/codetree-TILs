from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

num_count = {}
for i in range(n):
    if base[i] in num_count:
        num_count[base[i]] += 1
    else:
        num_count[base[i]] = 1

# print(num_count)
total = 0
for elem in num_count.keys():
    if k-elem == elem: #같은 값인 경우은 1번만 불려짐
        total += 2 #순서 상관없어서 중복을 2로 나눠서 처리!
    elif k-elem in num_count: #다른 값인 경우은 k-elem, elem으로 숫자가 2번 불려짐
        total += 1
print(total // 2)