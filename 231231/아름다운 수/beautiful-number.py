from sys import stdin
n = int(stdin.readline())
answer = []
total = 0

def check(answer):
    q = answer[0]
    count = 0
    for i in range(n):
        if q == answer[i]:
            count += 1
            if count > answer[i]:
                return False
        else:
            if count != answer[i]:
                return False
            count = 1
    
    #마지막 경우
    if count != answer[i]:
        return False
    return True

def solve(length):
    global total
    if length == n:
        if check(answer):
            total += 1
        return
    for i in range(1, 4+1):
        answer.append(i)
        solve(length+1)
        answer.pop()
    
solve(0)
print(total)