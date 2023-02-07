
height = 5

for i in range(1, height + 1):
    result = ""
    result += "*" * (height - i)
    result += " " * (2 * i - 1)
    result += "*" * (height - i)
    print(result)