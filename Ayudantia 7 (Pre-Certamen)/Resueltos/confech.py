cantidad_U = int(input("Numero de universidades: "))
U_aceptacion = 0
U_empate = 0
U_rechazan = 0

for i in range(0, cantidad_U):
    print()
    nombre = input("Universidad: ")
    flag = True
    A = 0
    R = 0
    B = 0
    N = 0
    while flag:
        voto = input("Voto: ")
        # asumo que los votos siempre son A,R o N.
        # input siempre valido.
        if voto == "X":
            flag = False
        else:
            if voto == "A":
                A += 1
            elif voto == "R":
                R += 1
            elif voto == "B":
                B += 1
            else:
                N += 1
    print(nombre + ":", A, "aceptan,", R,
          "rechazan,", B, "blancos,", N, "nulos.")
    if A > R:
        U_aceptacion += 1
    elif A < R:
        U_rechazan += 1
    else:
        U_empate += 1

print()
print("Universidades que aceptan:", U_aceptacion)
print("Universidades que rechazan:", U_rechazan)
print("Universidades con empate:", U_empate)
