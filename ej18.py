
def matrices(n,x = 0,y = 0):
        if x == len(n):
            return
        if y == len(n[0]):
            matrices(n, x + 1, 0)
        else:
            print(n[x][y], end=' ')
            matrices(n, x, y + 1)
matrices([[1, 2, 3],[4, 5, 6],[7, 8, 9]])