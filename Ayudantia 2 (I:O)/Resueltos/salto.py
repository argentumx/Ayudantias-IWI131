from random import randint
from math import sqrt

d = float(input("Altura: "))
v_i = randint(0, 50)
print("Velocidad incial:", v_i, "[m/s]")
a = 9.8
v_f = sqrt(v_i ** 2 + 2 * a * d)
print("Velocidad final:", v_f, "[m/s]")
