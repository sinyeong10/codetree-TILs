from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

# def sol(idx):
#     min_value = float("inf")
#     if idx == n-1:
#         return 0

#     # print(idx,base[idx]+1, n-idx)
#     for i in range(1, min(base[idx]+1, n-idx)):
#         min_value = min(min_value, sol(idx+i)+1)
#     return min_value

def sol(idx):
    min_value = float("inf")
    #넘으면 그 이전에서 가능하다는 이야기이므로 i의 범위를 인덱스 범위내로 제한하지 않아도 됨!
    if idx >= n-1:
        return 0

    # print(idx,base[idx]+1, n-idx)
    for i in range(1, base[idx]+1):
        min_value = min(min_value, sol(idx+i)+1)
    return min_value

tmp = sol(0)
print(tmp if tmp != float("inf") else -1)