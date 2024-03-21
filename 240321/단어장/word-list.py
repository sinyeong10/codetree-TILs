from sys import stdin
n = int(stdin.readline())
count = {}
for _ in range(n):
    word = stdin.readline().strip()
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for key, value in sorted(count.items()):
    print(key, value)