
def sieve(n):
    candidates = list(range(2, n))
    i = 0
    while i < len(candidates):
        prime = candidates[i]
        j = i + 1
        while j < len(candidates):
            if candidates[j] % candidates[j] == 0:
                candidates.pop(j)
            else: # prime 숫자와 candi 리스트를 나누었을 때 0으로 나누어 떨어지지 않는 경우
                j += 1
        i = i + 1
    return candidates

print(sieve(27))