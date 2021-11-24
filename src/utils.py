def contarPares(n):
    """ Función que cuenta pares hasta n """
    contador = 0
    for i in range(n):
        if i % 2 == 0:
            print(i)
            contador += 1

    return contador


# Si son iguales (en cantidad de elementos), devuelve 0
# Si a es mayor que b devuelve 1
# Si a es menor que b devuelve -1
def  comparoListas (a, b):
    sizeA = len(a)
    sizeB = len(b)
    comparacion = 0
    if sizeA < sizeB:
        comparacion = -1
    elif sizeA > sizeB:
        comparacion = 1
    return comparacion

