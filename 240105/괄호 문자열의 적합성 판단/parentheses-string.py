from sys import stdin
base = stdin.readline().strip()

def check(base):
    tmp = []
    for elem in base:
        if elem == "(":
            tmp.append(elem)
        else:
            if not tmp: #없음
                return False
            tmp.pop()
    
    if tmp: #있음
        return False
    return True

print("Yes" if check(base) else "No")