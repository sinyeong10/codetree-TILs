from sys import stdin
A = stdin.readline().strip()

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

#초기 값
result = RLE()

for _ in range(len(A)-2): #len(A)만큼 돔
    A = A[-1]+A[:-1]
    result = min(result, RLE())
    # print(A)
print(result)