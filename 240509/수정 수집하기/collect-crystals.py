from sys import stdin
n, k = list(map(int, stdin.readline().split()))
base = stdin.readline().strip()

data = []

last = "L"
cnt = 0
for i in range(n):
    if base[i] == last:
        cnt += 1
    else:
        data.append((base[i-1], cnt))
        last = base[i]
        cnt = 1
data.append((base[-1], cnt))
# print(data)

#i는 data에서 마지막으로 본 위치, j는 현재 위치, k는 이동 횟수
dp = [[[-1 for _ in range(2)] for _ in range(k+1)] for _ in range(len(data))]

trans = {"L":0, "R":1}
here = "L"
if data[0][0] == here: #L인 경우
    dp[0][0][0] = data[0][1]
    dp[0][1][1] = 0
else: #R인 경우
    dp[0][1][1] = data[0][1]
    dp[0][0][0] = 0
# print(dp)

for cnt in range(k+1):
    for i in range(len(data)-1):
        for j in range(2):
            if dp[i][j][cnt] == -1: #불가능
                # print("불가능",i,j,cnt)
                continue
            # print("가능",i,j,cnt,dp[i][j][cnt])
            if j == trans[data[i+1][0]]: #같으면 그대로 가서 점수 획득
                dp[i+1][j][cnt] = max(dp[i+1][j][cnt], dp[i][j][cnt]+data[i+1][1])
            else:
                dp[i+1][j][cnt] = max(dp[i+1][j][cnt], dp[i][j][cnt])
                if cnt < k:
                    dp[i+1][1-j][cnt+1] = max(dp[i+1][1-j][cnt+1], dp[i][j][cnt]+data[i+1][1])
# print(dp)
# print(list(max(elem) for elem in dp[-1]))
print(max(max(elem) for elem in dp[-1]))