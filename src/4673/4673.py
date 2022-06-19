def d(n: int) -> int:
    a = len(str(n))
    if a == 1:
        result = n + n
    elif a == 2:
        a, b = map(int, list(str(n)))
        result = n + a + b
    elif a == 3:
        a, b, c = map(int, list(str(n)))
        result = n + a + b + c
    elif a == 4:
        a, b, c, d = map(int, list(str(n)))
        result = n + a + b + c + d
    else:
        a, b, c, d, f = map(int, list(str(n)))
        result = n + a + b + c + d + f
    return result


b = list(range(1, 10001))

for x in range(1, 10001):
    a = d(x)
    if a in b:
        b.remove(a)

for a in b:
    print(a)
