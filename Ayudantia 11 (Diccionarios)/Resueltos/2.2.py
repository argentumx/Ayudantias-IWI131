caesar = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'g': 't', 'h': 'u',
          'i': 'v', 'j': 'w', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
          's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'y': 'l', 'z': 'm',
          'A': 'N', 'B': 'O', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U',
          'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'Q': 'D', 'R': 'E',
          'S': 'F', 'T': 'G', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M',
          'e': 'r', 'f': 's', 'k': 'x', 'l': 'y', 'q': 'd', 'r': 'e',
          'w': 'j', 'x': 'k', 'C': 'P', 'D': 'Q', 'I': 'V', 'J': 'W',
          'O': 'B', 'P': 'C', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K',
          'Y': 'L', 'Z': 'M'}


def cifrar(mensaje):
    cifrado = ""
    for letra in mensaje:
        if letra in caesar:
            for clave in caesar:
                letra_corrida = caesar[clave]
                if letra_corrida == letra:
                    cifrado += clave
        else:
            cifrado += letra
    return cifrado


a_cifrar = input("Ingrese el mensaje a cifrar: ")
print(cifrar(a_cifrar))
