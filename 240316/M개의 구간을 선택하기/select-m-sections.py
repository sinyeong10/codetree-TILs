from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

#처음을 선택하지 않는 경우가 없음
# all_results = []
# def backtrack(area, total, last_idx):
#     print(area, total, last_idx)
#     if area == m:
#         all_results.append(total)
#         return
#     now = 0
#     for i in range(last_idx + 2, n):
#         if i == 0:
#             now = base[i]
#         else:
#             now = max(base[i], now + base[i])
#         backtrack(area + 1, total + now, i)
#     return
# backtrack(0, 0, -2)
# print(all_results)

#다시 보니 틀림..
# ans = []
# import sys
# def sol(idx, cnt):
#     total = -sys.maxsize

#     if cnt == m: #m-1가 되고 바로 끝나면 안됨!
#         total = 0
#         for i in range(len(ans)):
#             total += ans[i]
#         # print("값", idx, cnt, ans, total)
#         return total

#     if cnt > m or idx >= n: #범위 초과
#         # print("멈춤", idx, cnt, ans)
#         return total
#     # print(idx, cnt, ans)
    
#     #현재 값 선택 안하고 넘어감!
#     total = max(total, sol(idx+1, cnt))

#     # 현재 인덱스 선택
#     if ans and ans[-1] != base[idx-1]: #이전 값이 있고, 현재 선택 바로 전의 값이 아닌 경우
#         cnt += 1
#     if not ans:
#         cnt += 1
#     ans.append(base[idx])
#     total = max(total, sol(idx+1, cnt))
#     ans.pop()

#     return total

# print(sol(0,0))

#그럼 이것도 틀림...
# ans = []
# import sys
# def sol(idx, cnt, total):
#     # total = -sys.maxsize

#     if cnt == m: #m-1가 되고 바로 끝나면 안됨!
#         print("값", idx, cnt, total, ans)
#         return total

#     if cnt > m or idx >= n: #범위 초과
#         # print("멈춤", idx, cnt, ans)
#         return -sys.maxsize
#     print(idx, cnt, total, ans)
    
#     #현재 값 선택 안하고 넘어감!
#     total = max(total, sol(idx+1, cnt, total))

#     # 현재 인덱스 선택
#     if ans and ans[-1] != base[idx-1]: #이전 값이 있고, 현재 선택 바로 전의 값이 아닌 경우
#         cnt += 1
#     if not ans:
#         cnt += 1
#     ans.append(base[idx])
#     total = max(total, sol(idx+1, cnt, total+base[idx]))
#     ans.pop()

#     return total

# print(sol(0,0,0))