"""
Una de las técnicas de criptografía más rudimentarias consiste en sustituir cada uno de los caracteres
por otro situado N posiciones más a la derecha.

Si `n = 2`, por ejemplo, sustituiremos la ((a)) por la ((c)), la ((b)) por la ((d)), y así sucesivamente.

El problema que aparece en las últimas n letras del alfabeto tiene fácil solución:
    en el ejemplo, la letra ((y)) se sustituirá por la ((a)) y la letra ((z)) por la ((b)).

La sustitución debe aplicarse a las letras minúsculas y mayúsculas y a los dígitos (el ((0)) se sustituye por el ((2)), el ((1))
por el ((3)) y así hasta llegar al ((9)), que se sustituye por el ((1))).

Diseña un programa que lea un texto y el valor de N y muestre su versión criptográfica.

ABCDEF
123456


NOTE:  ESTO ES UNA PRUEBA DE QUE NO FUNCIONA, NO SE COMO HACERLO, PERO NO FUNCIONA
"""
from string import ascii_lowercase

def conversor():
    for char in TEXT:
        pos = ascii_lowercase.index(char)
        if pos+N > len(ascii_lowercase):
            pos = len(ascii_lowercase) - (len(ascii_lowercase) + pos+N)
        return ascii_lowercase[pos+N]


TEXT = input("Introduce un texto: ")
N = int(input("Introduce el valor de N: "))

texto_cifrado = conversor()
print(f"Texto cifrado: {texto_cifrado}")



# def cifrar_texto(texto, n):
#     resultado = []
#     for caracter in texto:
#         # ASI SOLO FALTARÍA INCLUR LOS CASOS DE 9->1, Y->A, Z->B (mayus y minus)
#         if 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z':
#             resultado.append(chr((ord(caracter) + n)))
#         elif '0' <= caracter <= '9':
#             resultado.append(chr((ord(caracter) + n)))
#         else:
#             resultado.append(caracter)
#     return ''.join(resultado)
#
# texto = input("Introduce un texto: ")
# n = int(input("Introduce el valor de n: "))
# texto_cifrado = cifrar_texto(texto, n)
# print(f"Texto cifrado: {texto_cifrado}")
