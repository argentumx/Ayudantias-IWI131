clientes = {'16034124-5': ('Fernando Ruiz Diaz', 30, 'Vina', (100, 200, 300)),
            '5436576-2': ('Mike Portnoy', 20, 'Quilpue', (100, 100, 50)),
            '3333333-3': ('Slash', 50, 'Vina', (500, 550, 300)),
            '1234567-8': ('Cliff Burton', 35, 'Valparaiso', (10, 10, 100))}


def misma_sucursal(RUT1, RUT2, clientes):
    if clientes[RUT1][-2] == clientes[RUT2][-2]:
        return True
    return False


print(misma_sucursal('16034124-5', '3333333-3', clientes))
print(misma_sucursal('5436576-2', '3333333-3', clientes))


def mayores_que(edad_minima, clientes):
    lista = []
    for rut in clientes:
        nombre, edad, _, _ = clientes[rut]
        if edad >= edad_minima:
            lista.append(nombre)
    return lista


print(mayores_que(50, clientes))
print(mayores_que(25, clientes))


def es_cliente_vip(RUT, monto_compra, clientes):
    nombre, _, _, compras = clientes[RUT]
    sum_compra = 0
    for compra in compras:
        sum_compra += compra
    if sum_compra >= monto_compra:
        return True
    return False


print(es_cliente_vip('5436576-2', 500, clientes))
print(es_cliente_vip('3333333-3', 500, clientes))
print(es_cliente_vip('1234567-8', 150, clientes))
