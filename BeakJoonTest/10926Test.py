# a = input()
# if len(a) < 50: print(f'{a}??!')

# 18108번
# 서기 연도 입력 ex: 1998
# y = int(input())
# print(f'{y - 543}')

# 3003번
# 각각의 변수들이 같이 입력받아 각각 int형으로 저장된다.
# a, b, c, d, e, f = map(int, input().split(" "))
# print(f'{1-a} {1-b} {2-c} {2-d} {2-e} {8-f}')

# 10430번

A, B, C = map(int, input().split())
print((A + B) % C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)