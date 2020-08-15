def costo_total_paciente(rut):
    a = open("atenciones.txt", "r")
    suma = 0
    for linea in a:
        r, _, costo = linea.strip().split(":")
        if rut == r:
            suma += int(costo)
    a.close()
    return suma


def pacientes_dia(dia, mes, anio):
    a1 = open("atenciones.txt", "r")
    lista_ruts = []
    lista_pacientes = []
    for linea in a1:
        rut, fecha, _ = linea.strip().split(":")
        d, m, a = fecha.split("-")
        if int(d) == dia and int(m) == mes and int(a) == anio:
            lista_ruts.append(rut)
    a1.close()
    a2 = open("pacientes.txt", "r")
    for linea in a2:
        rut, nombre, _ = linea.strip().split(":")
        if rut in lista_ruts:
            lista_pacientes.append(nombre)
    a2.close()
    return lista_pacientes


print(costo_total_paciente('8015253-1'))
print(costo_total_paciente('14350739-4'))

print(pacientes_dia(2, 6, 2010))
print(pacientes_dia(23, 6, 2010))


def separar_pacientes():
    a = open("pacientes.txt", "r")
    jovenes = open("jovenes.txt", "w")
    mayores = open("mayores.txt", "w")
    for linea in a:
        rut, nombre, edad = linea.strip().split(":")
        if int(edad) < 30:
            jovenes.write(linea)
        else:
            mayores.write(linea)
    a.close()
    jovenes.close()
    mayores.close()


def ganancias_por_mes():
    a = open("atenciones.txt", "r")
    por_mes = []
    for i in range(0, 12):
        por_mes.append(0)
    for linea in a:
        _, fecha, costo = linea.strip().split(":")
        fecha = fecha.split("-")
        mes = int(fecha[1])
        por_mes[mes - 1] += int(costo)
    a.close()
    ganancia = open("ganancias.txt", "w")
    for i in range(0, 12):
        if por_mes[i] > 0:
            nueva_linea = ":".join([str(i + 1), str(por_mes[i])])
            ganancia.write(nueva_linea + "\n")
    ganancia.close()


separar_pacientes()
ganancias_por_mes()
