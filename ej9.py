def logaritmo(n,m):
        if n == 0:
            return 1
        if n == 1:
            return 0
        else:
            return logaritmo(n / m, m) + 1

print(logaritmo(32,2))