def vector(n):
        if not n:
            return []
        else:
            return [n[-1]] + vector(n[:-1])
print(vector([3, 4, 5, 6]))
