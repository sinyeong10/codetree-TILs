from sys import stdin
n = int(stdin.readline())
B = [int(stdin.readline()) for _ in range(n)]
B.sort(reverse = True)

# print(B)

total = 0
num = set()
count = 2*n
for elem in B:
    if elem < count: #최대 카드로 이길 수 있음!
        total += 1
        num.add(elem) #B가 사용한 카드 이제 못씀
    num.add(count) #A가 이긴 카드는 이제 못씀, 혹은 A가 졌을 때 B가 사용한 카드 중복 처리됨
    while count in num:
        count -= 1
    # print(elem, count, num, total)
print(total)