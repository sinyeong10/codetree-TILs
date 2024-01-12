from sys import stdin
n, m = list(map(int, stdin.readline().split()))

answer = []

def solve(idx, current_num): #idx는 현재 갯수, current_num은 현재 이 숫자까지 봄
    if idx == m:
        for elem in answer:
            print(elem, end=" ")
        print()
    
    for i in range(current_num+1, n+1):
        answer.append(i)
        solve(idx+1, i)
        answer.pop()


solve(0, 0)