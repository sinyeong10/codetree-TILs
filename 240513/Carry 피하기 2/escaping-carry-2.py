from sys import stdin
n =int(stdin.readline())
base = [int(stdin.readline()) for _ in range(n)]

ans = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            check = True
            a, b, c = base[i], base[j], base[k]
            standard = 10
            while not (a==b==c==0):
                # print(a,b,c)
                if a%standard+b%standard+c%standard >= 10: #1의 자리는 %10으로 구할 수 있음
                    check = False
                    break
                #매번 10으로 나눈 몫을 저장함!
                a //= standard
                b //= standard
                c //= standard
            if check:
                ans = max(ans, base[i]+base[j]+base[k])
print(ans)