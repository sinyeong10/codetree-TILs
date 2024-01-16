from sys import stdin
n = int(stdin.readline())

from sortedcontainers import SortedDict
sd = SortedDict()
for _ in range(n):
    sentence = stdin.readline().strip()
    if sentence in sd:
        sd[sentence] += 1
    else:
        sd[sentence] = 1

for key, value in sd.items():
    print(key, f"{value/n*100:.4f}")