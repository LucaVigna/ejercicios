def binaria(lista, n, m = 0):
        if not lista:
            return f"{n} No se encuentra en la lista"
        medio = len(lista) // 2
        if lista[medio] == n:
            return f"{n} Se encuentra en la posicion {m + medio + 1}"
        elif n < lista[medio]:
            return binaria(lista[:medio], n, m)
        else:
            return binaria(lista[medio + 1:], n, m + medio + 1)

lista = [1,2,3,4,5,6,7,8,9,10]
print(f"Ejemplo Primera mitad: {binaria(lista, 3)}")
print(f"Ejemplo Segunda mitad: {binaria(lista, 5)}")
print(f"Excepcion: {binaria(lista, 7)}\n")
