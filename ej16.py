def sucesion(n,m = 0):
        if n == (m + 1):
            return 2 - (3 * m)
        else:
            return sucesion(n,m + 1)
print(sucesion(7))
