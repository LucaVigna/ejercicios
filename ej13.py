def MCM (n,m,x = 1):
        if (n * x) % m == 0:
            return n * x
        else:
            return MCM(n,m,x + 1)
print(MCM(22,33))