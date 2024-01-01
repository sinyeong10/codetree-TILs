from sys import stdin
n = int(stdin.readline())
base = list(map(int, stdin.readline().split()))

def quick_sorting(base, low, high):
    pivot = base[low] #처음이 pivot
    i = low #이후 pivot보다 작은 값이 나올 시 바꿀 위치
    
    #순회하며 작은 값 나올시 바꿈
    for j in range(low+1, high+1): #low+1~high 비교대상
        if base[j] < pivot:
            i += 1 #다음 값을 큰값으로 생각, i전까지 작은 값으로 되어있다
            base[i], base[j] = base[j], base[i]

    #pivot을 중앙 기준으로 옮기고 기준점 반환
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