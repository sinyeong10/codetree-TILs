from sys import stdin
n = int(stdin.readline())
base = {}

for i in range(n):
    sentence = stdin.readline().strip()
    if sentence in base:
        base[sentence] += 1
    else:
        base[sentence] = 1

max_value = 0
for i in base.values():
    max_value = max(max_value , i)
print(max_value)