# def is_abecedarian(word):
#     for i in range(1, len(word)):
#         if word[i-1] > word[i]:
#             return False
#         return True
#
# f = open("C:/Users/수연/PycharmProjects/bc_python/8장_프로세싱/Words.txt", "r", encoding="UTF8")
#
# for line in f:
#     word = line.strip().lower()
#     if line[0] == "#":
#         continue
#     if is_abecedarian(word):
#         print(word)
# f.close()

# 연속된 동일한 문자 파악하기
# len(word)를 파악해서, word[i] 문자를 word[i+1]~word[len(word)-1] 문자까지 비교해서 똑같은게 나오면 count += 1 해주기? (이건 그냥 유사한 경우)
def three_doubles(word):
    for i in range(1, len(word)):
        s = ""
        if word[i-1] == word[i]:
            s += "*"
        else:
            s += " "
    return "* * *" in s

f = open("C:/Users/수연/PycharmProjects/bc_python/8장_프로세싱/Words.txt", "r", encoding="UTF8")

for line in f:
    word = line.strip().lower()
    three_doubles(word)
