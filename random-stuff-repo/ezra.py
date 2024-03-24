def fact(a, b, c, n):
    if c == n: return
    print(a)
    fact(b, a + b, c + 1, n)
fact(0, 1, 0, 10)