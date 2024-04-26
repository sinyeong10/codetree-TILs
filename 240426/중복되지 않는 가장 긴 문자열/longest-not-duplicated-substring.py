from sys import stdin
base = stdin.readline().strip()
# tmp = set()
# ans = 0
# end = 0
# for i in range(len(base)):
#     if base[i] not in tmp:
tmp = set(base)
print(len(tmp))