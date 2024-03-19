# from sys import stdin
# n, m = list(map(int, stdin.readline().split()))
# A = [stdin.readline() for _ in range(n)]
# B = [stdin.readline() for _ in range(n)]

# total = 0
# def check(idxs):
#     global total
#     tmpA = set()
#     for i in range(n):
#         key = ""
#         for j in idxs:
#             key += A[i][j]
#         tmpA.add(key)
    
#     for i in range(n):
#         key = ""
#         for j in idxs:
#             key += B[i][j]
#         if key in tmpA:
#             return 0
#     total += 1
#     return 1

# idxs = []
# #굳이 백트래킹 하지 않고, x,y,z를 중복되지 않게 구하는 for문 3중첩도 가능!
# def find_idx(idx, cnt):
#     if cnt > 4 or idx > m:
#         return

#     if cnt == 3:
#         check(idxs)
#         # if check(idxs):
#             # print(idxs)
#         return


#     find_idx(idx+1, cnt)
#     idxs.append(idx)
#     find_idx(idx+1, cnt+1)
#     idxs.pop()

# find_idx(0,0)
# print(total)

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

ans = 0
s = set()

def test_location(x, y, z):
    # x, y, z번째 자릿수를 선택했을 때 A와 B 그룹이
    # 완벽하게 구분되면 true, 그렇지 않다면 false를 반환합니다.
    s.clear()

    # A의 원소를 전부 HashSet에 넣어줍니다.
    for i in range(n):
        s.add(A[i][x:x + 1] + A[i][y:y + 1] + A[i][z:z + 1])
    
    # B의 원소 중 하나라도 A와 같은 경우가 있다면
    # A와 B를 구분해낼 수 없습니다.
    for i in range(n):
        if (B[i][x:x + 1] + B[i][y:y + 1] + B[i][z:z + 1]) in s:
            return False
    
    # 모든 B의 원소가 A와 다르다면 A와 B를 구분해낼 수 있습니다.
    return True

idxs = []
#굳이 백트래킹 하지 않고, x,y,z를 중복되지 않게 구하는 for문 3중첩도 가능!
def find_idx(idx, cnt):
    global ans
    if cnt > 4 or idx > m:
        return

    if cnt == 3:
        if test_location(idxs[0], idxs[1], idxs[2]): ans += 1
        return

    find_idx(idx+1, cnt)
    idxs.append(idx)
    find_idx(idx+1, cnt+1)
    idxs.pop()

find_idx(0,0)
            
# 두 그룹을 구분해낼 수 있는 조합 수를 출력합니다.
print(ans)