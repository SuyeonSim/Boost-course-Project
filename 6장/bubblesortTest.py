# 최적화 완료한 버블정렬
# 같은 int가 나왔을 경우 = 최적화 완료

def bubbleSort(a):
    sorted = False
    while (not sorted):
        sorted = True
        endnum = len(a) - 1
        while endnum > 0:
            last_swap = 0
            for i in range(1, endnum): # endnum을 설정하여, 만약 버블정렬을 시행한 리스트에서 순서대로 정렬이 되어있어 한번더 검사가 필요하지 않은 구간이 있다면 그 구간을 건너뛰고 필요한 구간만 버블정렬을 시행하도록 최적화
                if (a[i-1] > a[i]):
                    a[i-1], a[i] = a[i], a[i-1]
                    sorted = False
                    last_swap = i
                elif (a[i-1] == a[i]):
                    sorted = False
                    continue
            endnum = last_swap
    print(a)
a = [3, 2, 1, 4, 5]
bubbleSort(a)
