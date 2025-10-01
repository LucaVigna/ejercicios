def sumatoria(n):
        if n < 10:
            return n
        else:
            return (n % 10) + sumatoria(n // 10)
print(sumatoria(220))