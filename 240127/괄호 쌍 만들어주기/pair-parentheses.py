from sys import stdin
sentence = stdin.readline().strip()

count = 0 if sentence[-1] == "(" else 1
R = [0 for _ in range(len(sentence))]
for i in range(len(sentence)-2,-1,-1): #맨 마지막은 따로 처리
    if sentence[i] == ")":
        count += 1
        if count == 2:
            R[i] += R[i+1]+1
        else:
            R[i] = R[i+1]
    else:
        count = 0
        R[i] = R[i+1]
# print(sentence)
# print(R)

count = 0
answer = 0
for i in range(len(sentence)):
    if sentence[i] == "(":
        count += 1
        if count == 2:
            answer += R[i]
            count -= 1
    else:
        count = 0
print(answer)