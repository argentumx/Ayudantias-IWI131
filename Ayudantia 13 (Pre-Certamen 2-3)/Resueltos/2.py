def patentes_por_dueno(archivo_duenos):
    d = {}
    a = open(archivo_duenos, "r")
    for linea in a:
        nombre, patentes = linea.strip().split(";")
        patentes = patentes.split(",")
        cant = 0
        for patente in patentes:
            cant += 1
        d[nombre] = cant
    a.close()
    return d


print(patentes_por_dueno('info_duenos.txt'))


def patentes_multadas(archivo_registro, archivo_patentes):
    a1 = open(archivo_registro, "r")
    a2 = open(archivo_patentes, "r")
    lista = []
    for linea in a2:
        patente, TAG = linea.strip().split(",")
        if TAG == "0":
            a1 = open(archivo_registro, "r")
            for registro in a1:
                r = registro.strip()
                if r == patente:
                    lista.append(r)
            a1.close()
    a2.close()
    return lista


print(patentes_multadas('registro_diario.txt', 'patentes.txt'))


def personas_multadas(archivo_registro, archivo_patentes, archivo_duenos):
    lista = []
    multas = patentes_multadas(archivo_registro, archivo_patentes)
    a = open(archivo_duenos, "r")
    for linea in a:
        nombre, patentes = linea.strip().split(";")
        patentes = patentes.split(",")
        for patente in patentes:
            if patente in multas:
                if nombre not in lista:
                    lista.append(nombre)
    a.close()
    return lista


print(personas_multadas('registro_diario.txt', 'patentes.txt', 'info_duenos.txt'))
