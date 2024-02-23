from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

dp = [-1]*(m+1)
dp[0] = 1

#dict로 해당 key가 있는지 체크하면서 찾아갈 수도 있을듯!
def sol():
    for elem in base: #주어진 수를 순차적으로 고려
        for j in range(m, -1, -1): #역방향으로 안하면 계산한 값을 다시 사용
            #j를 기준으로 좌측을 보며 채워감
            #j가 elem보다 크다면 j-elem를 보고 가능하면 elem을 j-elem과 더해서 처리가능!
            # if j >= elem and dp[j-elem] == 1:
            #     dp[j] = 1

            #j를 기준으로 우측을 보며 채워감
            #j+elem이 목표인 수 m이하라면 j를 보고 가능하면 elem을 j와 더해서 처리가능!
            if dp[j] == 1 and j+elem <= m:
                dp[j+elem] = 1
        # print(elem, dp)
    return "Yes" if dp[m] == 1 else "No"

print(sol())