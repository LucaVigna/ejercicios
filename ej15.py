def raiz(n,m = 1):
        if n == 1 or n == 0:
            return n
        if m ** 2 == n:
            return m
        else:
            return raiz(n, m + 1)
print(raiz(9))