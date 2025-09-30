def multiplicacion(n,m):
        if m == 0 or n == 0:
            return 0
        elif m == 1:
            return n
        elif n == 1:
            return m
        else:
            return n + multiplicacion(n, m - 1)
print(multiplicacion(3,4))