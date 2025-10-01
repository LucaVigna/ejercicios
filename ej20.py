def centinela(lista,n,m = 0):
        if m == 0:
            lista.append(n)
        if n == lista[m]:
            if m == len(lista) - 1:
                return f"{n} No esta en la lista"
            else:
                return f"El numero {n} se encuentra en la lista en la posicion {m + 1}"
        else:
            return centinela(lista, n, m + 1)
        
lista = [7, 3, 4, 2]
print(f"Ejemplo verdadero: {centinela(lista,4)}")
print(f"Excepcion: {centinela(lista,50)}\n")