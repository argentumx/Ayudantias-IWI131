def suma_lineas(archivo):
    a = open(archivo, "r")
    lista = []
    for linea in a:
        valores = linea.strip().split(" ")
        aux_sum = 0
        for i in valores:
            aux_sum += int(i)
        lista.append(aux_sum)
    a.close()
    return lista


def suma_columnas(archivo):
    a = open(archivo, "r")
    # Nota: archivo de 3 columnas.
    # La suma-por-columna mas general tiene otra implementacion.
    lista = [0, 0, 0]
    for linea in a:
        valores = linea.strip().split(" ")
        for i in range(0, 3):
            lista[i] += int(valores[i])
    a.close()
    return lista


print(suma_lineas("datos1.txt"))
print(suma_columnas("datos1.txt"))
