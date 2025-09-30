def potencia(n,m):
        if n == 0:
            return 0
        elif m == 0 or n == 1:
            return 1
        elif m == 1:
            return n
        elif m < 0:
            return 1 / n * potencia(n, m + 1)
        else:
            return n * potencia(n, m - 1)

print(potencia(2,5))