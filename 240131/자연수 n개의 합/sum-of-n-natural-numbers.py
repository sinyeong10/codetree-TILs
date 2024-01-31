from sys import stdin
s = int(stdin.readline())

#1~n까지의 합은 n*(n+1)/2
def find(s):
    left = 1
    right = s
    max_index = 0
    while left<=right:
        mid = (left+right)//2
        if mid*(mid+1)/2 <= s: #s보다 mid로 계산한 결과가 작으므로 우측에 추가적으로 봐야함
            max_index = max(max_index, mid)
            left = mid+1
        else: #s보다 mid로 계산한 결과가 커서 좌측을 봐야함
            right = mid-1
    return max_index

print(find(s))