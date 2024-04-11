from sys import stdin
n = int(stdin.readline())
base = [stdin.readline().strip() for _ in range(n)]
# print(base)

#주먹, 가위, 보 순서!
L = [[0 for _ in range(n+1)] for _ in range(3)]
R = [[0 for _ in range(n+1)] for _ in range(3)]

#H:주먹, S:가위, P:보자기
#S,P,H가 base면 이김!

for i in range(n):
    if base[i] == "S":
        L[0][i+1] = L[0][i]+1
    else:
        L[0][i+1] = L[0][i]
    
    if base[i] == "P":
        L[1][i+1] = L[1][i]+1
    else:
        L[1][i+1] = L[1][i]
        
    if base[i] == "H":
        L[2][i+1] = L[2][i]+1
    else:
        L[2][i+1] = L[2][i]


for i in range(n-1, -1, -1): #base기준에 맞춘 후 R기준에 맞게 넣음
    if base[i] == "S":
        R[0][i] = R[0][i+1]+1
    else:
        R[0][i] = R[0][i+1]

    if base[i] == "P":
        R[1][i] = R[1][i+1]+1
    else:
        R[1][i] = R[1][i+1]
        
    if base[i] == "H":
        R[2][i] = R[2][i+1]+1
    else:
        R[2][i] = R[2][i+1]

# for i in range(3):
#     print(L[i])
#     print(R[i])

max_value = max(L[0][-1], L[1][-1], L[2][-1]) #하나를 쭉 하는 경우의 최대
for k in range(n): #k에서 바꿈
    for i in range(3): #왼쪽이 i인 경우
        for j in range(3): #오른쪽이 j인 경우
            # print(i,j)
            # print(i,k,j, L[i][k],R[j][k])
            max_value = max(max_value, L[i][k]+R[j][k])
print(max_value)