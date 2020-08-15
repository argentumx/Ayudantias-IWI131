def get_score(l):
    return l[1]

def get_name(l):
    return l[0]

def set_simulator(l):
    list_set = []
    for i in l:
        if i[1] not in list_set:
            list_set.append(i[1])
    return list_set

def print_list(l):
    for i in l:
        print(i)

# creacion de lista de listas, segun el enunciado
ll = []
n = int(input())
for x in range(n):
    name = input()
    score = float(input())
    ll.append([name, score])
# ordeno por el puntaje, de menor a mayor
ll.sort(key=get_score)

answer = []
# obtengo lista con puntajes unicos, sin repeticiones
s = set_simulator(ll)

# s[1] es el segundo minimo
# si len(s) = 1, todos obtuvieron el mismo puntaje y
# por ello, no hay segundo minimo.
if len(s) > 1:
    for li in ll:
        if get_score(li) == s[1]:
            answer.append(li[0])
answer.sort()
print_list(answer)
