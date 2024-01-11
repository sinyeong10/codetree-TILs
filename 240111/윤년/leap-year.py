from sys import stdin
year = int(stdin.readline())

def check(year):
    if (year%4==0 and year%100 != 0) or year%400 ==0:
        return True
    return False

print(1 if check(year) else 0)