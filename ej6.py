def invertir(palabra):
        if len(palabra) == 1:
            return palabra
        else:
            return invertir(palabra[1:]) + palabra[0]
print(invertir("mate"))