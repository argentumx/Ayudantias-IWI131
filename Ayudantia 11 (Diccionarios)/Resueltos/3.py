sansanos = {"Ana": (3, 1), "Jose": (4, 5), "Gonzalo": (6, 1)}

tiendas = {"Kiosko": ((3, 2), ["cafe", "jugos", "empanadas"]),
           "Food Truck": ((4, 1), ["hamburguesas"]),
           "Starbucks PUC": ((6, 4), ["cafe", "dulces"])}


def distancia_euclidiana(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


nombre_sansano = input("Ingrese el nombre de sansan@: ")
if nombre_sansano in sansanos:
    pos_sansano = sansanos[nombre_sansano]

    mindist = float('inf')
    tienda_elegida = ""
    for nombre in tiendas:
        pos_tienda, productos = tiendas[nombre]
        if "cafe" in productos:
            dist_atienda = distancia_euclidiana(pos_sansano, pos_tienda)
            if dist_atienda < mindist:
                mindist = dist_atienda
                tienda_elegida = nombre

    print("Tienda mas cercana a sansan@", nombre_sansano, "es", tienda_elegida)
else:
    print("Nombre no encontrado!")
