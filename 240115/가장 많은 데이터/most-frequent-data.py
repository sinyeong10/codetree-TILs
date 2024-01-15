from sys import stdin
n = int(stdin.readline())
base = {}

max_value = 0

for i in range(n):
    sentence = stdin.readline().strip()
    if sentence in base:
        base[sentence] += 1
    else:
        base[sentence] = 1
    max_value = max(max_value , base[sentence])
#for문으로 순회하는 대신 넣을 때 처리하는 것도 가능!
# for i in base.values():
#     max_value = max(max_value , i)

print(max_value)