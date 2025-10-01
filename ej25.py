def triangulo(n, m = 2, lista = [[1],[1,1]]):
        if len(lista) == n:
            for fila in lista:
                print(* fila)
            return lista
        fila = [1]
        for i in range(1, len(lista[-1])):
            fila.append(lista[-1][i - 1] + lista[-1][i])
        fila.append(1)
        lista.append(fila)
        return triangulo(n, m + 1, lista)
triangulo(11)