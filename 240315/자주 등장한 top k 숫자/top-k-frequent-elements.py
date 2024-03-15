from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base=list(map(int, stdin.readline().split()))

#숫자의 빈도 카운트
count = {}
for i in range(n):
    if base[i] in count:
        count[base[i]] += 1
    else:
        count[base[i]] = 1
# print(count)

#주어진 조건대로 정렬
tmp = []
for key in count.keys():
    tmp.append((count[key], key)) #등장 횟수 우선, 같으면 숫자 큰 것 우선!

tmp.sort(reverse=True) #내림차순 정렬

#k개 출력
for i in range(k):
    print(tmp[i][1], end=" ")