def existe_producto(codigo):
    a = open("productos.txt", "r")
    for linea in a:
        cod, _, _ = linea.strip().split("/")
        if int(cod) == codigo:
            return True
    return False


def por_reabstecer():
    a = open("productos.txt", "r")
    reabastecer = open("por_reabstecer.txt", "w")
    for linea in a:
        cod, nombre, unidad = linea.strip().split("/")
        if int(unidad) < 10:
            reabastecer.write(linea)
    a.close()
    reabastecer.close()


print(existe_producto(1784))
print(existe_producto(321))
print(existe_producto(613))
print(existe_producto(0))
por_reabstecer()
