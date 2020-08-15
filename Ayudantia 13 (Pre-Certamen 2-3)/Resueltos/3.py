def calcular_total(archivo_receta):
    a_receta = open(archivo_receta, "r")
    count = 1
    dicc = {}
    receta = (archivo_receta.split("-")[1]).split(".")[0]
    a_nutricion = open("NUTRICION-" + receta + ".txt", "w")
    for linea in a_receta:
        if count == 1:
            peso = float(linea.strip())
            receta = receta.split("_")
            receta = " ".join(receta)
            # primera linea contiene nombre de receta, peso
            # y segunda - 10 asteriscos
            a_nutricion.write(",".join([receta, str(peso) + "\n"]))
            a_nutricion.write("*" * 10 + "\n")
            count += 1
        else:
            producto, cantidad = linea.strip().split(" ")
            # abro archivo para revisar materia prima
            # de cada ingrediente
            arch_aux = open(producto + ".txt", "r")
            count += 1
            count_aux = 1
            for l in arch_aux:
                if count_aux == 1:
                    _, _, porcion = l.strip().split(",")
                    count_aux += 1
                else:
                    count_aux += 1
                    ingrediente, cant = l.strip().split(" ")
                    # cantidad de materia prima sigue proporcion
                    # cantidad_ingrediente/ porcion * cantidad_receta
                    cantidad_proporcional = (
                        float(cant) / float(porcion)) * float(cantidad)
                    # deccionario de forma INGREDIENTE:CANTIDAD
                    if ingrediente not in dicc:
                        dicc[ingrediente] = cantidad_proporcional
                    else:
                        dicc[ingrediente] += cantidad_proporcional
            arch_aux.close()
    a_receta.close()
    for ing in dicc:
        a_nutricion.write(" ".join([ing, str(dicc[ing]) + "\n"]))
    a_nutricion.close()


calcular_total("RECETA-CHOCOLATE_CON_MENTA.txt")
