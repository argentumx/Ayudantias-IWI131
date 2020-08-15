flag = True
suma = 0
cont = 0
while flag:
    i = input("Ingrese un numero: ")
    if i == "x": #alternativamente, if i.isnumeric() == False (no es solo numeros)
        flag = False
    else: #solo numeros enteros sin otros simbolos (no acepta negativos)
        suma += int(i)
        cont += 1
        promedio = suma / cont
        print(promedio)
print("Promedio muestral:", promedio)
