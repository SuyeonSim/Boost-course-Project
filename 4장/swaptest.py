def swap(a, b):
    a, b = b, a
    print(a, b)

x, y = 123, 456
swap(x, y)

def avg(data, start = 0, end = None):
    if not end:
        end = len(data)
    return sum(data[start:end]) / float(end-start)

d = (3, 4, 5, 6, 7)
d2 = d[1:3]
result = avg(d, 1, 4)
result2 = avg(d, 3)
print(result)
print(result2)


a = "Letter A"

def f(a):
    print("A= ", a)

def g():
    a = 5
    f(a + 1)
    print("A= ", a)

print("A= ", a)
f(3.14)
print("A= ", a)
g()
print("A= ", a)
