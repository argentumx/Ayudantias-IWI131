def get_palabra(palabra, clave):
    if clave not in palabra:
        return -1
    else:
        # de enunciado, se debe usar get_pos
        # como no lo tenemos y quiero correr el
        # programa, hago el simulador de get_pos.
        sub_index = s.find(clave)
        return s[0:sub_index] + s[sub_index + len(clave):]


print(get_palabra("foniwida", "iwi"))
print(get_palabra("iwien", "iwi"))
print(get_palabra("fiesta", "iwi"))


clave = input("Ingrese clave: ")
flag = True
mensaje_final = ''
while flag:
    palabra = input("Ingrese palabra: ")
    if palabra == "out":
        flag = False
    else:
        decifrado = get_palabra(palabra, clave)
        # str() aqui es casi innecesario, pero si fuera > o < si lo es.
        # es porque int siempre es menor que string porque int < string.
        if str(decifrado) != "-1":
            mensaje_final += get_palabra(palabra, clave) + " "
print("El mensaje oculto es:", mensaje_final)
