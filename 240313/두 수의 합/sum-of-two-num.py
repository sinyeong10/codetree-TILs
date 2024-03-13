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
        total += num_count[elem]*(num_count[elem]-1) #1번 불려질 때 n개라면 nC2만큼 가능!
    elif k-elem in num_count: #다른 값인 경우은 k-elem, elem으로 숫자가 2번 불려짐
        total += num_count[elem]*num_count[k-elem]
print(total // 2) #이후 중복을 2로 나눠서 처리