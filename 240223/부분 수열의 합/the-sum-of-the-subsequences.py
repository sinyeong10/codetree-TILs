from sys import stdin
n, m = list(map(int, stdin.readline().split()))
base = list(map(int, stdin.readline().split()))

dp = [-1]*(m+1)
dp[0] = 1

#dict로 해당 key가 있는지 체크하면서 찾아갈 수도 있을듯!
def sol():
    for elem in base:
        for j in range(m, -1, -1): #역방향으로 안하면 계산한 값을 다시 사용
            if dp[j] == 1 and j+elem <= m:
                dp[j+elem] = 1
        # print(elem, dp)
    return "Yes" if dp[m] == 1 else "No"

print(sol())