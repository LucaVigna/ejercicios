def fuerza(mochila, m = 0):
        if m == (len(mochila) - 1):
            return "No se ha encontrado el sable de luz", f"Objetos encontrados: {mochila}"
        if mochila[m] == "Sable":
            return "Se encontro el sable de luz", f"Fue necesario retirar otros {m} objetos"
        else:
            return fuerza(mochila, m + 1)

mochila = ["Augusto", "Comida", "registro", "Sable", "comunicador"]
mochila2 = ["tralalero", "navemini", "tele", "comunicador"]
print(f"Ejemplo con sable de luz: {fuerza(mochila)}")
print(f"Excepcion: {fuerza(mochila2)}\n")