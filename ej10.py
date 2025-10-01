def contador(n):
        if n < 10:
            return 1
        else:
            return 1 + contador(n // 10)

print(contador(48))