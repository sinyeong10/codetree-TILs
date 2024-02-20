from sys import stdin
base = stdin.readline().strip()

word = set()
for elem in base:
    if "a"<=elem<='f':
        word.add(elem)
word = list(word)
# print(word)

def check(case):
    j = 0
    total = case[base[0]]
    for i in range(1, len(base)):
        if base[i] == "+":
            total += case[base[i+1]]
        elif base[i] == "-":
            total -= case[base[i+1]]
        elif base[i] == "*":
            total *= case[base[i+1]]
        else:
            j+=1
            continue
    # print(case, total)
    return total

case = {}
def sol(idx):
    max_value = float("-inf") #음수도 답이 될 수 있음!
    if idx == len(word):
        max_value = max(max_value, check(case))
        return max_value
    
    for i in range(1, 5):
        case[word[idx]] = i
        max_value = max(max_value, sol(idx+1))
        case.pop(word[idx])
    return max_value

print(sol(0))