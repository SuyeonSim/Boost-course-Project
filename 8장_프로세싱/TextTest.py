planets = [] # planets 이라고 하는 리스트 만들어주기
f = open("C:/Users/수연/Desktop/파이썬_부스트코스/Planets.txt", "r")
# s = f.readline()
# print(s) # 한줄만 읽음

current = 0
earth = 0

# for line in f:
#     s = line.strip() # 개행 문자를 제거하고
#     planets = s
#     print(planets) # 개행 문자를 제거하고, print문을 실행했을 때의 줄바꿈 또한 없애줬음

for line in f:
    current += 1
    planet = line.strip().lower()
    if planet == 'arth':
        print("Earth is planet #%d" % current)
        break
    else:
        print("Not found")
        break