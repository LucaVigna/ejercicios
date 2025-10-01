def torre(n, x, y, z):
        if n == 1:
            return [f"Mover disco 1 de {x} a {y}"] 
        else:
            return (
                torre(n - 1, x, z, y) +
                [f"Mover disco {n} de {x} a {y}"] +
                torre(n - 1, z, y, x))
        
probar = torre(3, "Aguja 1", "Aguja 3", "Aguja 2")
for t in probar:
    print(t)