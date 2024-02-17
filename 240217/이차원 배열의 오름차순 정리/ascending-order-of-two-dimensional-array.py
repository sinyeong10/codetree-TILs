from sys import stdin
n = int(stdin.readline())
k = int(stdin.readline())

#1~n까지의 범위!

#1 2 3 4
#2 4 6 8 
#3 6 9 12
#4 8 12 16

total = []
for i in range(1, n+1):
    for j in range(1, n+1):
        total.append(i*j)
total.sort()
print(total[k-1])

# left = 0
# right = n*n-1
# while left<=right:
#     mid = (left+right)//2
#     if mid < k:

#     elif mid > k:
    
#     elif mid == k: