from sys import stdin
s = stdin.readline().strip()
p = stdin.readline().strip()

new_p = []
fix = False
key = "!"
for j in range(len(p)-1,-1,-1):
    if p[j] == "*":
        fix = True
        key = p[j-1]
        new_p.append(p[j])
        new_p.append(p[j-1])
    
    # if fix and p[j] == key:
    #     continue
    
    elif p[j] != key:
        fix = False
        new_p.append(p[j])

# print(new_p)

p = "".join(new_p[::-1])
# print(p)

def solve():
    i_last = len(s)-1
    j_last = len(p)-1
    #뒤부터 채워가야  .*a와 같은 경우 처리 가능!
    while j_last >= 0:
        # print(i_last, j_last)
        if i_last < 0:
            return False
        if s[i_last] == p[j_last] or p[j_last] == ".":
            i_last-=1
            j_last-=1
        elif p[j_last] == "*":
            check = True
            while i_last >= 0 and (p[j_last-1] == s[i_last] or p[j_last-1] == "."):
                i_last -= 1
                check = False
            if check:
                return False
            j_last -= 2
        else:
            return False
    return True

print("true" if solve() else "false")