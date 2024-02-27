from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

def sol(idx, count, total): #현재보는 base의 idx와 현재까지 선택한 수 count, 현재까지 계산값
    # print(idx, count, total)
    if count == m: #m개를 다 선택하여 계산함
        return total
    if idx == n: #base를 다 봄
        return 0 #최댓값을 찾기에 없다는 의미로 0을 반환
    tmp = 0
    # #idx를 선택하는 경우
    # if count == 0: #처음에는 xor연산이 이뤄지지 않고 값이 그대로 들어감
    #     tmp = max(tmp, sol(idx+1, count+1, base[idx]))
    # else:
    tmp = max(tmp, sol(idx+1, count+1, total^base[idx])) #0과 숫자의 xor 연산의 결과는 숫자임!
    #idx를 선택하지 않는 경우
    tmp = max(tmp, sol(idx+1, count, total))
    return tmp

print(sol(0,0,0))