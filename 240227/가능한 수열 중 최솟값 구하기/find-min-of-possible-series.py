from sys import stdin
n = int(stdin.readline())

check = True
ans = []
# def sol(idx):
#     global check
#     if not check:
#         return
#     if idx == n:
#         for elem in ans:
#             print(elem, end="")
#         print()
#         check = False
#         return
    
#     for i in range(4,7):
#         tmp = True
#         if len(ans) >= 1 and i == ans[-1]:
#             tmp = False
#             continue
        
#         for j in range((idx+1)//2-1): #홀수 시 보는 범위 증가!
#             # print(ans, i,j,ans[-(3+j)-j:-1-j], ans[-1-j:] + [i])
#             if ans[-(3+j)-j:-1-j] == ans[-1-j:] + [i]:
#                 tmp = False
#                 break

#             # if len(ans) >= 5 and ans[-5:-2] == ans[-2:] + i:
#             #     tmp = False
#             #     break
#             #...
#         if tmp:
#             ans.append(i)
#             sol(idx+1)
#             ans.pop()
#     return

# #i를 먼저 넣고 계산할 수 있다!
# def sol(idx):
#     global check
#     if not check:
#         return
#     if idx == n:
#         for elem in ans:
#             print(elem, end="")
#         print()
#         check = False
#         return
    
#     for i in range(4,7):
#         tmp = True
#         if len(ans) >= 1 and i == ans[-1]:
#             tmp = False
#             continue
        
#         ans.append(i)
#         j = 0
#         while True: #idx는 마지막 전 위치와 같음
#             if ans[idx-j:] == ans[idx-2*j-1:idx-j]:
#                 tmp = False
#                 break
#             j+=1
#             if idx-2*j-1 < 0:
#                 break

#         if tmp:
#             sol(idx+1)
#         ans.pop()
#     return

# sol(0)


def sol(idx):
    if idx == n:
        for elem in ans:
            print(elem, end="")
        print()
        return True #값이 출력됨
    
    for i in range(4,7):
        tmp = True
        if len(ans) >= 1 and i == ans[-1]: #1개 비교
            continue

        for j in range(1, (idx+1)//2): #홀수 시 보는 범위 증가!
            if ans[-j-(j+1):-j] == ans[-j:] + [i]: #마지막 j개+[i]와 j+1개를 비교
                tmp = False
                break

            # if len(ans) >= 5 and ans[-5:-2] == ans[-2:] + i:
            #     tmp = False
            #     break
            #...
        if tmp:
            ans.append(i)
            if sol(idx+1):
                return True
            ans.pop()
    return False

sol(0)