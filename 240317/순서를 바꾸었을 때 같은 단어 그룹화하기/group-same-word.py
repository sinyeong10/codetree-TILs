from sys import stdin
n = int(stdin.readline())
group = {}
for _ in range(n):
    word = stdin.readline().strip()
    tmp = {}
    for elem in word:
        if elem in tmp:
            tmp[elem]+=1
        else:
            tmp[elem] = 1
    
    ans = ""
    for key in sorted(tmp.keys()): #알파벳순서로 key를 정렬해서 순서를 동일하게 함!
        ans = ans+str(key)+str(tmp[key])
    # print(ans)

    if ans in group:
        group[ans] += 1
    else:
        group[ans] = 1

# print(group)

max_value = 0
many_word = ""
for key, value in group.items():
    if max_value < value:
        max_value = value
        many_word = key
# print(many_word)
print(max_value)

#가장 많은 그룹의 단어의 길이가 아닌 갯수임...
# length = 0
# for i in range(1, len(many_word), 2):
#     length += int(many_word[i])
# print(length)