from sys import stdin
n, m, k = list(map(int, stdin.readline().split()))
action = list(map(int, stdin.readline().split()))

move_map = [1 for _ in range(k)]

ans = 0
#k를 1개씩 n번 선택

def back_track(cnt):
    # print(cnt, move_map)
    global ans
    if cnt == n:
        partical_ans = 0
        for elem in move_map:
            if elem >= m:
                partical_ans += 1
        ans = max(ans, partical_ans)
        return
    
    last_check = True
    for idx in range(k):
        if move_map[idx] >= m:
            continue
        last_check = False
        move_map[idx] += action[cnt]
        back_track(cnt+1) #n-1까지 들어가고 n에서 체크함
        move_map[idx] -= action[cnt]


    if last_check:
        # print(last_check, move_map)
        partical_ans = 0
        for elem in move_map:
            if elem >= m:
                partical_ans += 1
        ans = max(ans, partical_ans)
        return


back_track(0)

print(ans)