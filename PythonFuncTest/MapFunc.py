import math
A, B = map(int, input().split())
if A > 0:
    if B < 10:
        print(A + B)
# 리스트를 float -> int
result1 = list(map(int, [1.1, 2.2, 3.3, 4.4, 5.5]))
print(f'map(int, 리스트) : {result1}')
# x의 5제곱을 반환
def func_pow(x):
    return pow(x, 5)
result2 = list(map(func_pow, [1, 2, 3, 4, 5]))
print(f'map(func_pow, 리스트) : {result2}')
# 리스트 값 소수점 올림
result3 = list(map(math.ceil, [1.1, 2.2, 3.3, 4.4, 5.5]))
print(f'map(func_ceil, 리스트) : {result3}')
# map함수: map(function, iterable(반복 가능한 자료형. 리스트, 튜플 등))