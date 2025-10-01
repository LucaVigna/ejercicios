
def MCD(n,m):
        if m == 0:
            return n
        else:
            return MCD(m, n % m) 
print(MCD(540,320))