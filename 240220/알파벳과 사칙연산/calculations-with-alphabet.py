from sys import stdin
base = stdin.readline().strip()

word = set()
for elem in base:
    if "a"<=elem<='f':
        word.add(elem)
# print(word)

def check(case):
    j = 0
    total = case[j]
    for i in range(1, len(base)):
        if base[i] == "+":
            total += case[j+1]
        elif base[i] == "-":
            total -= case[j+1]
        elif base[i] == "*":
            total *= case[j+1]
        else:
            j+=1
            continue
    return total

case = []
def sol(idx):
    max_value = 0
    if idx == len(word):
        max_value = max(max_value, check(case))
        return max_value
    
    for i in range(1, 5):
        case.append(i)
        max_value = max(max_value, sol(idx+1))
        case.pop()
    return max_value

print(sol(0))