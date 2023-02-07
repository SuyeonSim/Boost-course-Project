
# useryear = input("최대/최소 환율을 알고 싶은 연도를 입력: ")

years = range(1994, 2010)

def read_year(yr, data):
    f = open("C:/Users/수연/Desktop/파이썬_부스트코스/data/%d.txt" % yr, "r")
    for line in f:
        data1, value1 = line.split("          ")
        date = data1.split("/")
        yr_month_date = 10000 * int(date[0]) + 100 * int(date[1]) + int(date[2])
    # 달러를 원화로 바꿔준다.
        v = float(value1)
        v2 = int(1/v)
    # data 리스트에 더해준다.
        data.append((yr_month_date, v2))
    f.close()
# 1994년부터 2010년까지 모든 년도를 저장하는 큰 리스트를 생성한다.
def read_all():
    data = [] # 리스트 생성
    for yr in years:
        read_year(yr, data) # data 리스트에 (yyyymmdd, 환율) 튜플을 추가.
    return data # 만들어진 리스트를 return
# 연도별로 평균 환율 계산(compute)
def average(data, yr): # data: (yyyymmdd, 환율)이 있는 리스트. yr: 1994년~2010년
    sum = 0
    count = 0
    start = yr * 10000 # 예: 1994 -> 19940000
    end = (yr + 1) * 10000 # 1995 -> 19950000
    for d, v in data:
        if start <= d < end: # 19940000 <= d < 19950000 (1994년도것만 계산)
            sum += v
            count += 1
    return sum / count # 1994년도의 모든 v를 더한 후 count(day)로 나눔

#월별 최대/최소 환율 알아보기
# def find_minmax(yr):
#     minmax = [(9999), 0] * 12
#     # data = read_year(yr) # 몇년도의 정보를 알아볼건지 정리하기
#     data = read_year(yr)
#     for d, v in data: # d: 8자리의 integer, y: 환율
#         month = (d // 100) % 100 - 1
#         minr = maxr = minmax[month]
#         if v < minr:
#             minr = v
#         if v > maxr: maxr = v
#             maxr = v
#         minmax[month] = minr, maxr
#     return minmax

def find_min(data): # 최소 환율을 찾는 함수
    vm = 99999 # 초기 설정값
    dm = None # yyyymmdd
    for d, v in data: # 이 과정을 1994~2010까지 반복하기
        if v < vm: # 예: v < 99999 (초기 설정값보다는 무조건 적음)
            vm = v # 현재의 vm보다 v가 작다면 대체
            dm = d # 날짜도 대체
    return dm, vm

def find_max(data): # 최대 환율을 찾는 함수
    vm = 0
    dm = None
    for d, v in data:
        if v > vm: # 만약 v가 현재의 vm(value max)보다 크다면
            vm = v # v로 대체
            dm = d
    return dm, vm

def main():
    data = read_all() # 1994년도~2010년도의 날짜와 환율 리스트를 return
    print("Min:", find_min(data))
    print("Max:", find_max(data))
    for yr in years: # 연도별로 환율 평균값을 알아보기
        avg = average(data, yr)
        print(yr, avg)

main()