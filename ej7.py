def sumatoria(n):
        if n == 1:
            return n
        else:
            return 1 / n + sumatoria(n - 1)

print(sumatoria(3))