from sys import stdin
n = int(stdin.readline())
data = [[i]+list(map(int, stdin.readline().split())) for i in range(n)]
data.sort(key=lambda x : (x[1],x[0])) #먼저 온 순서, 기다릴때는 번호표 순서로 입장
print(data)

time = 0 #현재 시간
ans = 0
import heapq
hq = []
#첫번째 경우, a가 같은 시점이 있어도 무조건 정렬 기준상 처음으로 들어감!
num, a, t = data[0]
# print("현재 들어감", num, a,t)
time = a+t
check = a

for idx in range(1, n):
    # print(idx, hq)
    if data[idx][1] <= time: #앞이 아직 안 끝나는 경우 대기열에 추가 [이미 hq에 값이 있는 경우에 time이 같은 시점은 여기서 걸려짐]
        heapq.heappush(hq, data[idx])
        continue

    if hq: #대기열이 있으면 같이 들어가서 계산해야 하는 같은 시점[chekc]이 아니고 time보다 현재 시작 시점이 늦을 때까지만 돎
        while check != data[idx][1] and data[idx][1] > time:
            #같이 시작하는 사람이 다 오고[정렬되어 작은 것에서 달라지면 시작임] 이전에 들어간 사람이 끝남 #이전 대기열 처리해야 함
            if hq:
                num, a, t = heapq.heappop(hq)
                # print("현재 들어감", num, a,t, end=" : ")
                ans = max(ans, time-a) #들어가는 시간에서 처음 온 시간이 기다린 시간
                time = max(time+t, a+t) #앞사람이 끝나고 바로 시작하지 않을 수 있음!
                #끝난시간+현재 들어가서 걸리는 시간 / 끝난 후에 시간이 흐르고 들어가서 걸리는 시간
                # print(check, time)
            else: #다보면 빠져 나옴
                break
    else: #처음 대기열에 들어감
        check = data[idx][1]

    heapq.heappush(hq, data[idx])
    
#다 대기중이면 이제 대기중에서 순차적으로 빠짐
while hq:
    num, a, t = heapq.heappop(hq)
    # print("현재 들어감", num, a,t)
    ans = max(ans, time-a) #들어가는 시간에서 처음 온 시간이 기다린 시간
    time += t #끝난시간+현재 들어가서 걸리는 시간

print(ans)