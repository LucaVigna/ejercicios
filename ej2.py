def suma(n):
        if n == 0 or n == 1:
            return n
        else:
            return n + suma(n - 1)
print(suma(4))