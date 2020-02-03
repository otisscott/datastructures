def fibs(n):
    s, l = 1, 1
    for num in range(n):
        yield s
        s, l = l, s + l
