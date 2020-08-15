dif = input("Ingrese la dificultad: ")

if dif == "facil":
    n = 3
elif dif == "media":
    n = 5
else:
    n = 7

t_total = 0
v_min = float('inf') #o un numero muy grande, como 9999999
v_max  = -float('inf') # o un numero muy chico, -9999999

while(n):
    t = int(input("Tiempo empleado: "))
    v =  float(input("Velocidad de estudiante: "))
    t_total += t
    if v < v_min:
        v_min = v
    elif v > v_max:
        v_max = v
    n -= 1

print("Tiempo:", t_total, "[s]")
print("V max:", v_max, "[m/s]")
print("V min:", v_min, "[m/s]")
