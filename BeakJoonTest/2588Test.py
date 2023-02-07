# int형 리스트 생성 완료. len()을 활용하여 하나씩 곱해줌.
A = int(input())
B_list = list(map(int, str(input())))
r3 = A * B_list[2]
print(r3)
r4 = A * B_list[1] * 10
print(r4 // 10)
r5 = A * B_list[0] * 100
print(r5 // 100)
print(r3 + r4 + r5)