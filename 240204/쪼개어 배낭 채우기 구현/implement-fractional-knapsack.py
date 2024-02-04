from sys import stdin
n, m = list(map(int, stdin.readline().split()))

base = []
for _ in range(n):
    w,v = list(map(int, stdin.readline().split()))
    e = v/w #무게 1당 가치를 계산해야함 따라서 가치를 무게로 나눔 #1:?=w,v => v/w
    base.append((-e, w, v)) #내림차순 정렬

base.sort() #내림차순 정렬을 여기서 새로운 변수 없이 key=lambda x: -x[1] / x[0]로 해도 됨!

total = 0
value = 0
for e, w, v in base:
    # if total+w <= m: #전체
    #     total += w
    #     value += v
    # else: #부분
    #     tmp_w = m-total
    #     total += tmp_w
    #     value += tmp_w*-e
    # if total == m:
    #     break

    #total 변수 없이 m에서 빼면서 처리!
    if m >= w: #전체
        m-=w
        value += v
    else: #부분
        value += m/w*v #m:?=w:v => m/w*v
        break
    
    # print(e,w,v)
    # print(total, value)
print(f"{value:.3f}")