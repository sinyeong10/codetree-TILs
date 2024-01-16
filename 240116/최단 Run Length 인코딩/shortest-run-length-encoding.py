from sys import stdin
A = stdin.readline().strip()

result = float("inf")

def RLE():
    stand = A[0]
    count = 0
    ans = ""
    for i in range(len(A)):
        if stand == A[i]:
            count += 1
        else:
            ans += stand+str(count)
            stand = A[i]
            count = 1
    #마지막 처리
    ans += stand+str(count)
    # print(ans)
    return len(ans)

for _ in range(len(A)):
    result = min(result, RLE())
    A = A[-1]+A[:-1]
    # print(A)
print(result)