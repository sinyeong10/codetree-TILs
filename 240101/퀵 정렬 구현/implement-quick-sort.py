from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

def quick_sorting(base, low, high):
    pivot = base[low]
    i = low
    
    for j in range(low+1, high+1): #low+1~high 비교대상
        if base[j] < pivot:
            i += 1
            base[i], base[j] = base[j], base[i]

    base[i], base[low] = base[low], base[i]
    return i    



def quick_sort(base, low, high):
    if low < high: #최소 원소 2개
        pos = quick_sorting(base, low, high) #피봇 골라 정렬
        #분할로 내려가 정렬
        quick_sort(base, low, pos-1)
        quick_sort(base, pos+1, high)

quick_sort(base, 0, len(base)-1)

print(* base)